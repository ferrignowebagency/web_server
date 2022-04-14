<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Nuovo cliente</h4>

                    <div class="page-title-right">
                        <ol class="breadcrumb m-0">
                            <li class="breadcrumb-item"><a href="javascript: void(0);">Tables</a></li>
                            <li class="breadcrumb-item active">Basic Tables</li>
                        </ol>
                    </div>

                </div>
            </div>
        </div>

        <div class="column is-12">
            <div class="row">
                <div class="col-lg-12 col-12">
                    <form @submit.prevent="submitForm">
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
                                                        <select v-model="type_client" class="form-control">
                                                            <option value="cliente">Cliente</option>
                                                            <option value="investitore">Investitore</option>
                                                            <option value="proprietario">Proprietario</option>
                                                        </select>
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Titolo</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <select v-model="client_title" class="form-control">
                                                            <option value="signore">Sig.</option>
                                                            <option value="signora">Investitore</option>
                                                            <option value="dottore">Dott.</option>
                                                            <option value="dottoressa">Dott.ssa</option>
                                                            <option value="Geometra">Geom.</option>
                                                        </select>
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Nome</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="name" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cognome</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="surname" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="form-group row" style="margin: 10px 0px;">
                                                <label style="" for="i_type_annuncio" class="col-sm-4 col-form-label col-form-label-sm">Agente</label>
                                                <div class="col-lg-6" style="justify-content: space-between;">
                                                    <select v-model="contact_person" class="form-control">
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
                                                        <input type="text" class="form-control" v-model="phone1" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 2</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="phone2" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Telefono 3</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="phone3" id="status_annuncio" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">E-mail</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="email" class="form-control" v-model="email" id="status_annuncio" placeholder="">
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
                                                <div class="col-md-9">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Indirizzo</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="address" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-3">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Civico</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="civico" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Zona</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="zona" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Comune</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="comune" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Provincia</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="provincia" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-6">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Regione</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="regione" placeholder="">
                                                    </div>
                                                </div>
                                            </div>

                                            <div class="row g-3" style="margin: 10px 0px;">
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-4 col-form-label col-form-label-sm">Cap</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="zip_code" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Longitudine</label>
                                                    <div class="col-md-12">
                                                        <input type="text" class="form-control" v-model="latitude" placeholder="">
                                                    </div>
                                                </div>
                                                <div class="col-md-4">
                                                    <label style="" for="i_titolo" class="col-sm-6 col-form-label col-form-label-sm">Latitudine</label>
                                                    <div class="col-lg-12" style="justify-content: space-between;">
                                                        <input type="text" class="form-control" v-model="longitude" placeholder="">
                                                    </div>
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

                        <button class="btn btn-success btn-label"><i class="bx bx-save label-icon"></i>Salva</button>
                        <div style="margin:15px 0px;"></div>

                    </form>
                </div>
            </div>
        </div>
    </div>
</div>
</template>

<script>
import axios from 'axios'
import {
    useToast
} from "vue-toastification";
const toast = useToast();


export default {
    name: 'Add_client',
    data() {
        return {
            name: '',
            surname: '',
            contact_person: '',
            email: '',
            phone1: '',
            estimated_value: 0,
            website: '',
            type_client: '',
            client_title: '',
            phone2: '',
            phone3: '',
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
                const errors = []

                if (this.name === '') {
                    errors.push('Il campo nome è vuoto')
                }

                if (this.email === '') {
                    errors.push('Il campo email è vuoto')
                }

                if (this.phone1 === '') {
                    errors.push('Il campo Telefono 1 è vuoto')
                }
                if (this.contact_person === '') {
                    errors.push('Il campo contact person 1 è vuoto')
                }
                console.log(errors)
                
            this.$store.commit('setIsLoading', true)

            const client = {
                name: this.name,
                sur_name: this.surname,
                phone1: this.phone1,
                contact_person: this.contact_person,
                email: this.email,
                phone2: this.phone2,
                phone3: this.phone3,
                type_client: this.type_client,
                client_title: this.client_title,
                website: this.website,
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
                .post('/api/v1/clients/', client)
                .then(response => {
                    toast.success("Cliente creato")

                    this.$router.push('/dashboard/clienti')
                })
                .catch(error => {
                    if (error.response) {
                                for (const error in errors) {
                                    //this.errors.push(`${property}: ${error.response.data[property]}`)
                                    toast.error(error.toString)
                                    console.log(error)
                                }                 
                                    
                                }
                            
                    
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
