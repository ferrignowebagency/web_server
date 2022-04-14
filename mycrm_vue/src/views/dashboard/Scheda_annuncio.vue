<template>
<div class="container fade-in-load">
    <div class="columns is-multiline">
        <div class="column is-12">
            <h1 class="title">ERA-{{ annuncio.id }}</h1>

            <router-link :to="{ name: 'Edit_annuncio', params:annuncio.id}" class="button is-light">Edit</router-link>
        </div>

        <div class="column is-12">
            <div class="row">
                <div class="col-lg-10 col-12">

                    <div class="card" style="margin:15px 0px;">
                        <h6 style="background-color: #ced4da; padding:15px;" class="card-title mb-4">#1 - Principale
                        </h6>
                        <div class="card-body">

                            <div class="row">
                                <div class="col-lg-6 ">

                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Dettagli immobile</h4>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_titolo" class="col-sm-4 col-form-label">Titolo</label>
                                            <div class="col-lg-12" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.title">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_descrizione" class="col-sm-4 col-form-label">
                                                Descrizione</label>
                                            <div class="col-lg-12" style="justify-content: flex-end">
                                                <textarea disabled row="15" class="form-control" v-model="annuncio.descrizione"></textarea>
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="status_annuncio" class="col-sm-4 col-form-label">Stato annuncio</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" placeholder="" value="Attivo">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_type_annuncio" class="col-sm-4 col-form-label">Tipologia</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" v-model="annuncio.type_immobile" class="form-control">

                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_off_min" class="col-sm-4 col-form-label">Off.
                                                Minima</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.prezzo_quattro">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_prezzo_base" class="col-sm-4 col-form-label">Prezzo Base</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.prezzo_due">
                                            </div>
                                        </div>
                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_val_stimato" class="col-sm-4 col-form-label">Valore stimato</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.prezzo_tre">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_val_stimato" class="col-sm-4 col-form-label">Quality Rating</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.quality">
                                            </div>
                                        </div>

                                    </div>

                                </div>
                                <div class="col-lg-6">

                                </div>
                            </div>
                        </div>
                    </div>

                    <div class="card" style="margin:15px 0px;">
                        <h6 style="background-color: #ced4da; padding:15px;" id="02" class="card-title mb-4">#2 -
                            Luogo</h6>
                        <div class="card-body">
                            <div class="row">
                                <div class="col-lg-6">
                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Dati geografici</h4>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_indirizzo" class="col-sm-4 col-form-label">Indirizzo</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.address">
                                            </div>
                                        </div>
                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_indirizzo" class="col-sm-4 col-form-label">Civico</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.civico">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_zona" class="col-sm-4 col-form-label">
                                                Zona</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.zona">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_comune" class="col-sm-4 col-form-label">
                                                Comune</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.comune">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_provincia" class="col-sm-4 col-form-label">Provincia</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.provincia">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_regione" class="col-sm-4 col-form-label">Regione</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.regione">
                                            </div>
                                        </div>

                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_cap" class="col-sm-4 col-form-label">CAP</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.zip_code">
                                            </div>
                                        </div>
                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_cap" class="col-sm-4 col-form-label">CAP</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.latitude">
                                            </div>
                                        </div>
                                        <div class="form-group row input-form-ctsm">
                                            <label style="" for="i_cap" class="col-sm-4 col-form-label">CAP</label>
                                            <div class="col-lg-6" style="justify-content: flex-end">
                                                <input disabled type="text" class="form-control" v-model="annuncio.longitude">
                                            </div>
                                        </div>

                                    </div>
                                </div>
                                <div class="col-lg-6">
                                    <div class="card-body shadowed">
                                        <h4 class="card-title mt-0">Mappa</h4>
                                        <iframe width="100%" height="300" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="https://www.openstreetmap.org/export/embed.html?bbox=-8.613281250000002%2C37.49229399862877%2C28.081054687500004%2C51.68617954855624&amp;layer=mapnik&amp;marker=45.0113%2C9.11575"></iframe>
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
</template>

<script>
import axios from 'axios'

export default {
    name: 'Annuncio',
    data() {
        return {
            annuncio: {}
        }
    },
    mounted() {
        this.getAnnuncio()
    },
    methods: {
        async getAnnuncio() {
            this.$store.commit('setIsLoading', true)
            const annuncioID = this.$route.params.id

            await axios
                .get(`/api/v1/annunci/${annuncioID}/`)
                .then(response => {
                    this.annuncio = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
