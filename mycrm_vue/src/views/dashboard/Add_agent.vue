<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Add agent</h1>
            </div>

            <div class="column is-6">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Email</label>
                        <div class="control">
                            <input type="email" name="email" class="input" v-model="username">
                        </div>
                    </div>

                   <!-- <div class="field">
                        <label>Nome</label>
                        <div class="control">
                            <input type="test" name="first_name" class="input" v-model="first_name">
                        </div>
                    </div>

                    <div class="field">
                        <label>Cognome</label>
                        <div class="control">
                            <input type="text" name="last_name" class="input" v-model="last_name">
                        </div>
                    </div> -->

                    <div class="field">
                        <label>Password</label>
                        <div class="control">
                            <input type="password" name="password1" class="input" v-model="password1">
                            
                        </div>
                    </div> 


                    <div class="field">
                        <label>Repeat password</label>
                        <div class="control">
                            <input type="password" name="password2" class="input" v-model="password2">
                        </div>
                    </div>

                    <div class="notification is-danger" v-if="errors.length">
                        <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Submit</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import {toast} from 'bulma-toast'

export default {
    name: 'Add_agent',
    data() {
        return {
            username: '',
            password1: '',
            password2: '',
            errors: []
        }
    },
    methods: {
        async submitForm() {
            this.errors = []

            if (this.username === '') {
                this.errors.push('Il campo nome utente è vuoto!')
                }

           
            if (this.password1 === '') {
                this.errors.push('La password è troppo corta!')
            }

            if (this.password1 !== this.password2) {
                this.errors.push('Le password non coincidono!')
            }

            if (!this.errors.length) {
                this.$store.commit('setIsLoading', true)

                const formData = {
                    username: this.username,
                    password: this.password1,
                }

                await axios
                    .post('/api/v1/users/', formData)
                    .then(response => {
                        toast({
                            message: 'Nuovo agente creato',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        const emailData = {
                            'email': this.username,
                        }

                        axios
                            .post('/api/v1/agency/add_agent/', emailData)
                            .then(response => {
                                this.$router.push({'name': 'Lista_agenzie'})
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

                this.$store.commit('setIsLoading', false)
            }
        }
    }
}

</script>