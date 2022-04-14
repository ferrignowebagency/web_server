<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <form @submit.prevent="submitForm">
            <div class="row">
                <div class="col-12">
                    <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                        <h4 class="mb-sm-0 font-size-18">Scheda Modifica {{ client.name }} {{ client.surname }}</h4>

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
                                    <div class="col-lg-6 ">

                                        <div class="card-body shadowed">
                                            <h4 class="card-title mt-0">Dettagli Cliente</h4>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Tipologia</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <select v-model="client.type" class="form-select">
                                                            <option value="cliente">Cliente</option>
                                                            <option value="investitore">Investitore</option>
                                                            <option value="proprietario">Proprietario</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Titolo</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <select v-model="client.title" class="form-select">
                                                            <option value="signore">Sig.</option>
                                                            <option value="signora">Sig.ra</option>
                                                            <option value="dottore">Dott.</option>
                                                            <option value="dottoressa">Dott.ssa</option>
                                                            <option value="geometra">Geom.</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Nome</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.name" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cognome</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.surname" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_type_annuncio" class="col-sm-4 col-form-label col-form-label-sm">Agente</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <select v-model="client.contact_person" class="form-control">
                                                        <option value="appartamento">Appartamento</option>
                                                        <option value="villa">Villa</option>
                                                        <option value="terreno">Terreno</option>
                                                        <option value="negozio">Negozio</option>

                                                    </select>
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
                                                        <input type="text" class="form-control" v-model="client.phone1" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 2</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.phone2" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 3</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.phone3" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">E-mail</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="email" class="form-control" v-model="client.email" id="status_annuncio" placeholder="">
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
                                        <div class="card-body" style="background-color:#f5f5f5">
                                            <h4 class="card-title mt-0">Dati geografici</h4>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-12">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Indirizzo intelligente</label>
                                                    <div class="col-md-12">
                                                        <vue-google-autocomplete ref="address" id="map" classname="form-control" placeholder="Inserisci l'indirizzo" v-on:placechanged="getAddressData" country="it"></vue-google-autocomplete>
                                                    </div>
                                                </div>
                                                <div class="col-md-8">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Indirizzo</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="client.address" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Civico</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.civico" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Zona</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="client.zona" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Comune</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.comune" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Provincia</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="client.provincia" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Regione</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.regione" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cap</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="client.zip_code" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Longitudine</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="client.latitude" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Latitudine</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="client.longitude" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                        </div>
                                    </div>
                                    <div class="col-lg-6">
                                        <div class="card-body" style="background-color:#f5f5f5">
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
            </div>
        </form>
    </div>
</div>
</template>

<script>
import axios from 'axios'

import GMAPMARKER from '@/components/gmapmarker.vue'

import {
    useToast
} from "vue-toastification";
import VueGoogleAutocomplete from "vue-google-autocomplete";
const toast = useToast();
export default {
    components: {
        VueGoogleAutocomplete,
        GMAPMARKER
    },

    name: 'EditClient',
    data() {
        return {
            client: {}
        }
    },
    mounted() {
        this.getClient()
        // To demonstrate functionality of exposed component functions
        // Here we make focus on the user input
        this.$refs.address.focus();
        //this.$refs.city.focus();
    },
    methods: {
        /**
         * When the location found
         * @param {Object} addressData Data of the found location
         * @param {Object} placeResultData PlaceResult object
         * @param {String} id Input container ID
         */

        getAddressData: function (addressData, placeResultData, id) {
            this.client.address = addressData.route;
            this.client.civico = addressData.street_number;
            this.client.comune = addressData.locality;
            this.client.provincia = addressData.administrative_area_level_2;
            this.client.regione = addressData.administrative_area_level_1;
            this.client.zip_code = addressData.postal_code;
            this.client.latitude = addressData.latitude;
            this.client.longitude = addressData.longitude;
            console.log(addressData)
        },
        async getClient() {
            this.$store.commit('setIsLoading', true)

            const clientID = this.$route.params.id

            axios
                .get(`/api/v1/clients/${clientID}/`)
                .then(response => {
                    this.client = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        },

        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const clientID = this.$route.params.id

            axios
                .patch(`/api/v1/clients/${clientID}/`, this.client)
                .then(response => {
                    toast.success("Scheda aggiornata")

                    this.$router.push(`/dashboard/clienti/${clientID}`)
                })
                .catch(error => {
                    toast.error(error)
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    },
}
</script>
