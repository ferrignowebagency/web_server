

<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Lista annunci</h4>

                    <div class="page-title-right">
                        <ol class="breadcrumb m-0">
                            <li class="breadcrumb-item"><a href="javascript: void(0);">Tables</a></li>
                            <li class="breadcrumb-item active">Basic Tables</li>
                        </ol>
                    </div>

                </div>
            </div>
        </div>

                                <PlaceSearch
  v-bind:ready="ready"
  placeholder="Enter a location"
  loading="Map is loading"
  v-bind:fallbackProcedure="fallbackProcedure"
  v-bind:zoom="zoom"
  v-bind:geolocation="geolocation"
  v-bind:gps_timeout="3000"
  v-bind:address="address"
  @changed="getMapData"
>
</PlaceSearch>

        <div class="column is-12">
            <div class="row">
                <div class="col-lg-10 col-12">
                    <form @submit.prevent="submitForm">
                        <div class="card" style="margin:15px 0px;">
                            <h6 class="card-title mb-4">#1 - Principale
                            </h6>
                            <div class="card-body">

                                <div class="row">
                                    <div class="col-lg-6 ">

                                        <div class="card-body shadowed">
                                            <h4 class="card-title mt-0">Dettagli immobile</h4>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Titolo</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="title">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_descrizione" class="col-sm-4 col-form-label col-form-label-sm">
                                                    Descrizione</label>
                                                <div class="col-lg-12" style="justify-content: space-between;">
                                                    <textarea row="15" class="form-control" v-model="descrizione"></textarea>
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="status_annuncio" class="col-sm-4 col-form-label col-form-label-sm">Stato annuncio</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" id="status_annuncio" placeholder="" value="Attivo">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_type_annuncio" class="col-sm-4 col-form-label col-form-label-sm">Tipologia</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <select v-model="type_immobile" class="form-control">
                                                        <option value="appartamento">Appartamento</option>
                                                        <option value="villa">Villa</option>
                                                        <option value="terreno">Terreno</option>
                                                        <option value="negozio">Negozio</option>

                                                    </select>
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_off_min" class="col-sm-4 col-form-label col-form-label-sm">Off.
                                                    Minima</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="prezzo_quattro">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_prezzo_base" class="col-sm-4 col-form-label col-form-label-sm">Prezzo Base</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="prezzo_due">
                                                </div>
                                            </div>
                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_val_stimato" class="col-sm-4 col-form-label col-form-label-sm">Valore stimato</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="prezzo_tre">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_val_stimato" class="col-sm-4 col-form-label col-form-label-sm">Quality Rating</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="quality">
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
                            <h6 id="02" class="card-title mb-4">#2 -
                                Luogo</h6>
                            <div class="card-body">
                                <div class="row">
                                    <div class="col-lg-6">
                                        <div class="card-body shadowed">
                                            <h4 class="card-title mt-0">Dati geografici</h4>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                               <!-- <label style="" for="i_indirizzo" class="col-sm-4 col-form-label col-form-label-sm">Indirizzo</label>-->
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                     <label class="col-span-2 block text-sm font-medium text-gray-700">
      Street
                                                    <input class="form-control" type="text" @input="$emit('update:street', $event.target.value)" :value="street" ref="streetRef" placeholder="Street" />
                                                    </label>
                                                </div>
                                            </div>
                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_indirizzo" class="col-sm-4 col-form-label col-form-label-sm">Civico</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <label class="col-span-2 block text-sm font-medium text-gray-700">
                                                    <input class="form-control" type="text" @input="$emit('update:streetNumber', $event.target.value)" :value="streetNumber" placeholder="Number" />
                                                    </label>
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_zona" class="col-sm-4 col-form-label col-form-label-sm">
                                                    Zona</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="zona">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_comune" class="col-sm-4 col-form-label col-form-label-sm">
                                                    Comune</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input class="form-control" type="text" @input="$emit('update:city', $event.target.value)" :value="city" placeholder="City" />

                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_provincia" class="col-sm-4 col-form-label col-form-label-sm">Provincia</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="provincia">
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_regione" class="col-sm-4 col-form-label col-form-label-sm">Regione</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input class="" type="text" @input="$emit('update:country', $event.target.value)" :value="country" placeholder="Country" />

                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_cap" class="col-sm-4 col-form-label col-form-label-sm">CAP</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input class="" type="text" @input="$emit('update:postcode', $event.target.value)" :value="postcode" placeholder="Postcode" />
                                                </div>
                                            </div>
                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_cap" class="col-sm-4 col-form-label col-form-label-sm">Latitudine</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="latitude">
                                                </div>
                                            </div>
                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_cap" class="col-sm-4 col-form-label col-form-label-sm">Longitudine</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <input type="text" class="form-control" v-model="longitude">
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



                        <button class="button is-success">Submit</button>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
/*
import {
    ref,
    computed
} from 'vue' */

import {onMounted, onUnmounted,ref} from "vue";

import comuni from '/src/misc/comuni.json'
import countries from '/src/misc/countries.json'

import {
    toast
} from 'bulma-toast'

export default {
    name: 'Add_annuncio',
    data() {
        return {
            company: '12',
            contact_person: '12',
            email: '12@gmail.com',
            phone: '12121',
            estimated_value: 0,
            confidence: 0,
            website: '',
            title: '',
            descrizione: '',
            type_immobile: '',
            prezzo_uno: '',
            prezzo_due: '',
            prezzo_tre: '',
            prezzo_quattro: '',
            quality: '45',
            address: '',
            civico: '',
            zona: '',
            comune: '',
            provincia: '',
            regione: '',
            zip_code: '',
            latitude: '',
            longitude: '',
        }
    },
    methods: {
        async submitForm() {
            this.$store.commit('setIsLoading', true)

            const annuncio = {
                company: this.company,
                contact_person: this.contact_person,
                phone: this.phone,
                website: this.website,
                estimated_value: this.estimated_value,
                confidence: this.confidence,
                title: this.tile,
                descrizione: this.descrizione,
                type_immobile: this.type_immobile,
                prezzo_uno: this.prezzo_uno,
                prezzo_due: this.prezzo_due,
                prezzo_tre: this.prezzo_tre,
                prezzo_quattro: this.prezzo_quattro,
                quality: this.quality,
                address: this.address,
                civico: this.civico,
                zona: this.zona,
                comune: this.comune,
                provincia: this.provincia,
                regione: this.regione,
                zip_code: this.zip_code,
                latitude: this.latitude,
                longitude: this.longitude,
            }

            await axios
                .post('/api/v1/annunci/', annuncio)
                .then(response => {
                    toast({
                        message: 'Nuovo annuncio creato con successo',
                        type: 'is-success',
                        dismissible: true,
                        pauseOnHover: true,
                        duration: 2000,
                        position: 'bottom-right',
                    })

                    this.$router.push('/dashboard/annunci')
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    },
    /*
    setup() {

        let comune = ref('')
        let regione = ref('')
        var regione_field = ''
        const comuneobj = Object.values(comuni);
        const searchCountries = computed(() => {
            if (comune.value === '') {
                console.log(comuni[0])
                console.log(countries)
                //console.log(comuneobj)
                return []
            }
            let matches = 0

            let zip
            return comuni.filter(comune0 => {
                if (comune0.nome_comune.toLowerCase().includes(comune.value.toLowerCase()) && matches < 10) {
                    matches++
                    console.log(comune0.nome_comune)
                    regione_field = comune0.regione
                    console.log(regione_field)
                    return comune0.nome_comune
                }

            })
        });
        const selectcomune_field = (comune_field) => {
            selectedcomune_field.value = comune_field
            console.log(comune_field)
            comune.value = comune_field
            updateGeoData();
        }
        const updateGeoData = (comune_field) => {
            regione.value = regione_field
            //updateGeoData();
        }

        let selectedcomune_field = ref('')
        return {
            comuni,
            comune,
            searchCountries,
            selectcomune_field,
            selectedcomune_field
        }

    }, */

}
</script>
