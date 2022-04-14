<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Scheda cliente</h4>

                    <div class="page-title-right">
                        <router-link :to="{ name: 'Client_edit', params:client.id}" type="button" class="btn btn-primary waves-effect btn-label waves-light onlist-btn"> <i class="bx bx-pencil label-icon"></i>Modifica</router-link>

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
                                <div class="col-lg-6 ">

                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Dettagli Cliente</h4>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Tipologia</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.type">

                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Titolo</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.title">

                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Nome</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.name">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cognome</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.surname">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Agenzia</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.phone1">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Agente</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.phone2">
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                </div>
                                <div class="col-lg-6">

                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Contatti cliente</h4>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 1</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.phone1">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 2</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.phone2">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 3</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.phone3">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">E-mail</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="email" class="form-control" v-model="client.email">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Creazione</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" v-model="client.created_at"  class="form-control">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Ultima modifica</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.modified_at">
                                                </div>
                                            </div>
                                        </div>

                                    </div>

                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="margin:15px 0px;">
                        <h6 id="02" class="card-title mb-4">#2 -
                            Luogo</h6>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-lg-6">
                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Dati geografici</h4>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-8">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Indirizzo</label>
                                                <div class="col-md-12">
                                                    <input disabled type="text" class="form-control" v-model="client.address">
                                                </div>
                                            </div>
                                            <div class="col-md-4">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Civico</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.civico">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Zona</label>
                                                <div class="col-md-12">
                                                    <input disabled type="text" class="form-control" v-model="client.zona">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Comune</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.comune">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Provincia</label>
                                                <div class="col-md-12">
                                                    <input disabled type="text" class="form-control" v-model="client.provincia">
                                                </div>
                                            </div>
                                            <div class="col-md-6">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Regione</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" class="form-control" v-model="client.regione">
                                                </div>
                                            </div>
                                        </div>

                                        <div class="row g-3" style="margin: 10px 0px;">
                                            <div class="col-md-4">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cap</label>
                                                <div class="col-md-12">
                                                    <input disabled type="text" class="form-control" v-model="client.zip_code">
                                                </div>
                                            </div>
                                            <div class="col-md-4">
                                                <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Longitudine</label>
                                                <div class="col-md-12">
                                                    <input disabled type="text" limit="10" class="form-control" v-model="client.latitude">
                                                </div>
                                            </div>
                                            <div class="col-md-4">
                                                <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Latitudine</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input disabled type="text" limit="10" class="form-control" v-model="client.longitude">
                                                </div>
                                            </div>
                                        </div>

                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Mappa</h4>
                                        <GMAPMARKER />
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>

                    <div style="margin:15px 0px;"></div>

                </div>
            </div>
 
            <hr>
<div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Note private</h4>

                    <div class="page-title-right">
                        <router-link :to="{ name: 'Add_note', params:client.id}" type="button" class="btn btn-primary waves-effect btn-label waves-light onlist-btn"> <i class="bx bx-pencil label-icon"></i>Aggiungi nota</router-link>

                    </div>

                </div>
            </div>
        </div>
            <div class="col-lg-12 col-12">
                
               <div class="card-group">
                    <div class="card col-6" style="margin:15px 15px;"  v-for="note in notes" v-bind:key="note.id">
                        <header class="card-header border-bottom text-uppercase text-white" style="background:#153b65;">                            
                                {{ note.name }}                            
                            <div class="card-header-icon">
                                <span class="icon">
                                    <i class="fas fa-clock"></i>
                                </span>
                                <time datetime="2016-1-1">{{formatDateIT(note.created_at)}}</time>
                            </div>
                        </header>
                        <div class="card-body">
                            <div class="content">
                                {{ note.body }}
                                <br>
                                <time datetime="2016-1-1">{{formatDateIT(note.created_at)}}</time>
                            </div>
                        </div>
                        <footer class="card-footer bg-transparent border-top text-muted">
                            <router-link :to="{ name: 'Edit_note', params: { id: client.id, note_id: note.id }}" noteclass="card-footer-item" class="card-footer-item">Edit </router-link>
                            <a href="#" class="card-footer-item">Delete</a>
                        </footer>
                    </div>

                </div>
            </div> <!-- Blocco delle note -->
            <div class="space" style="margin:30px 0px;"></div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import moment from 'moment'
import GMAPMARKER from '@/components/gmapmarker.vue'

export default {
    name: 'Client',
    components: {
        GMAPMARKER},
    data() {
        return {
            client: {},
            notes: [],
            
        }
    },
    mounted() {
        this.getClient()
    },
    methods: {
        async getClient() {
            this.$store.commit('setIsLoading', true)

            const clientID = this.$route.params.id

            await axios
                .get(`/api/v1/clients/${clientID}/`)
                .then(response => {
                    this.client = response.data
                    
                })
                .catch(error => {
                    console.log(error)
                })
            await axios
                .get(`/api/v1/notes/?client_id=${clientID}`)
                .then(response => {
                    this.notes = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },
        formatDateIT(val) {
            return moment(val).format('DD/MM/YYYY, HH:mm:ss')
        }

    },

  watch: {
    'client.created_at': function(val, oldVal) {
        this.client.created_at = this.formatDateIT(val)
    },
    'client.modified_at': function(val, oldVal) {
        this.client.modified_at = this.formatDateIT(val)
    }
    }

    

}
</script>
