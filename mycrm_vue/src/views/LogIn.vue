<template>
    
<div class="account-pages my-5 pt-sm-5">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-md-6 col-lg-5 col-xl-3">
                    <div class="card overflow-hidden">
                        <div class="bg-primary bg-soft" style="background:#153b65!important;">
                            <div class="row">
                                <div class="col-7">
                                    <div class="text-primary p-4" style="color:#fff!important;">
                                        <h5 style="color:#fff!important;" class="text-primary">Bentornato</h5>
                                        <p style="color:#fff!important;">Inserisci le tue credenziali</p>
                                    </div>
                                </div>
                                <div class="col-5 align-self-end">
                                    <img src="assets/images/profile-img.png" alt="" class="img-fluid">
                                </div>
                            </div>
                        </div>
                        <div class="card-body pt-0">
                            <div class="auth-logo">
                                <a href="index.html" class="auth-logo-light">
                                    <div class="avatar-md profile-user-wid mb-4">
                                        <span class="avatar-title rounded-circle bg-light">
                                            <img src="assets/images/logo-light.svg" alt="" class="rounded-circle" height="34">
                                        </span>
                                    </div>
                                </a>

                                <a href="index.html" class="auth-logo-dark">
                                    <div class="avatar-md profile-user-wid mb-4">
                                        <span class="avatar-title rounded-circle bg-light">
                                            <img src="https://export.easyre.srl/wp-content/themes/twenty-twenty-one-child/easyre-favicon.png" alt="" class="rounded-circle" height="34">
                                        </span>
                                    </div>
                                </a>
                            </div>
                            <div class="p-2">
                                <form @submit.prevent="submitForm" class="form-horizontal">

                                    <div class="mb-3">
                                        <label for="username" class="form-label">Nome utente</label>
                                        <input type="email" class="form-control" id="username" placeholder="Il tuo nome utente" v-model="username">
                                    </div>

                                    <div class="mb-3">
                                        <label class="form-label">Password</label>
                                        <div class="input-group auth-pass-inputgroup">
                                            <input type="password" class="form-control" placeholder="La tua password" aria-label="Password" aria-describedby="password-addon" v-model="password">
                                            <button class="btn btn-light " type="button" id="password-addon"><i class="mdi mdi-eye-outline"></i></button>
                                        </div>
                                    </div>
                                    

                                    <div class="form-check">
                                        <input class="form-check-input" type="checkbox" id="remember-check">
                                        <label class="form-check-label" for="remember-check">
                                            Ricorda accesso
                                        </label>
                                    </div>
                                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                                    <div class="mt-3 d-grid">
                                        <button class="btn btn-primary waves-effect waves-light">Accedi</button>
                                    </div>

                                    
                                    <div class="mt-4 text-center">
                                        <a href="auth-recoverpw.html" class="text-muted"><i class="mdi mdi-lock me-1"></i> Password dimenticata?</a>
                                    </div>
                                </form>
                            </div>

                        </div>
                    </div>
                    <div class="mt-5 text-center">

                        <div>
                                                        <p>©
                                2022 Easyre. 
                            </p>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </div>
    
</template>



<script>
    import axios from 'axios'

    export default {
        name: 'LogIn',
        data() {
            return {
                username: '',
                password: '',
                errors: []
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                axios.defaults.headers.common['Authorization'] = ''
                localStorage.removeItem('token')

                const formData = {
                    username: this.username,
                    password: this.password
                }

                await axios
                    .post('/api/v1/token/login/', formData)
                    .then(response => {
                        const token = response.data.auth_token

                        this.$store.commit('setToken', token)

                        axios.defaults.headers.common['Authorization'] = 'Token ' + token

                        localStorage.setItem('token', token)
                    })
                    .catch(error => {
                        if (error.response) {
                            for (const property in error.response.data) {
                                this.errors.push(`${property}: ${error.response.data[property]}`)
                            }
                        } else if (error.message) {
                            this.errors.push('Something went wrong. Please try again!')
                        }
                    })

                await axios
                    .get('/api/v1/users/me')
                    .then(response => {
                        this.$store.commit('setUser', {'id': response.data.id, 'username': response.data.username})

                        localStorage.setItem('username', response.data.username)
                        localStorage.setItem('userid', response.data.id)
                    })
                    .catch(error => {
                        console.log(error)
                    })

                await axios
                    .get('/api/v1/agency/get_my_agency/')
                    .then(response => {
                        this.$store.commit('setAgency', {'id': response.data.id, 'name': response.data.name})

                        this.$router.push('/dashboard')
                    })
                    .catch(error => {
                        console.log(error)
                    })
                
                this.$store.commit('setIsLoading', false)
            }
        }
    }
</script>