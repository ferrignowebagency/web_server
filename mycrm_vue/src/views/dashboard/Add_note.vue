<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <form @submit.prevent="submitForm">
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                        <h4 class="mb-sm-0 font-size-18">Nuova nota</h4>

                        <div class="page-title-right">
                            <button class="btn btn-success btn-label"><i class="bx bx-save label-icon"></i>Salva</button>
                        </div>

                    </div>
                </div>
            </div>

            <div class="column is-12">
                <div class="row">
                    <div class="col-lg-12 col-12">

                        <div class="card" style="margin:15px 0px;">
                            <h6 class="card-title mb-4">#1 - Principale
                            </h6>
                            <div class="card-body">

                                <div class="row">
                                    <div class="col-lg-12">

                                        <div class="card-body shadowed">
                                            <h4 class="card-title mt-0">Dettagli Cliente</h4>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-12">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Titolo</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="name">
                                                    </div>
                                                </div>
                                                <div class="col-md-12">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Messaggio</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <textarea class="form-control" maxlength="225" rows="3" v-model="body"></textarea>
                                                    </div>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </form>
    </div>
</div>
</template>

<script>
import axios from 'axios'

import {
    toast
} from 'bulma-toast'

export default {
    name: 'AddNote',
    data() {
        return {
            name: '',
            body: ''
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const note = {
                name: this.name,
                body: this.body,
                client_id: this.$route.params.id
            }

            await axios
                .post('/api/v1/notes/', note)
                .then(response => {
                    toast({
                        message: 'The note was added',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push({
                        name: 'Client_det',
                        params: {
                            id: this.$route.params.id
                        }
                    })
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
