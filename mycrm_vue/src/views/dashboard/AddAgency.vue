<template>
    <div class="container">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Aggiungi Agenzia</h1>
            </div>

            <div class="column is-12">
                <form @submit.prevent="submitForm">
                    <div class="field">
                        <label>Nome Agenzia</label>
                        <div class="control">
                            <input type="text" class="input" v-model="name">
                        </div>
                    </div>

                    <div class="field">
                        <div class="control">
                            <button class="button is-success">Invia</button>
                        </div>
                    </div>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    import { toast } from 'bulma-toast'

    export default {
        name: 'AddAgency',
        data() {
            return {
                name: ''
            }
        },
        methods: {
            async submitForm() {
                this.$store.commit('setIsLoading', true)

                const agency = {
                    name: this.name
                }

                await axios
                    .post('/api/v1/agency/', agency)
                    .then(response => {
                        toast({
                            message: 'The agency was added',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })

                        this.$store.commit('setAgency', {'id': response.data.id, 'name': this.name})

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