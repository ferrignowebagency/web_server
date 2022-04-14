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
        <!-- end page title -->

        <div class="row">
            <div class="col-xl-12">
                <div class="card">
                    <div class="card-body">

                        <div class="d-flex justify-content-between align-items-center border-bottom text-uppercase" style="padding-top:0.75rem; padding-bottom:0.75rem;">
                            <div class="float-left">
                                <b>Totale:</b> <span class="badge bg-primary easyre-badge" id="countTOTAL">{{ annunci.length }}</span>
                                <b>Filtrati:</b> <span class="badge bg-primary easyre-badge green" id="countFILTER">0</span>
                                <b>Selezionati:</b> <span class="badge bg-primary easyre-badge orange" id="countSELECT">22</span>
                            </div>
                            <div class="float-end">
                                <router-link to="/dashboard/annunci/add" type="button" class="btn btn-primary filter-btn btn-label waves-light onlist-btn"> <i class="bx bx-filter-alt label-icon"></i>Filtri</router-link>
                                <router-link to="/dashboard/annunci/add" type="button" class="btn btn-primary waves-effect btn-label waves-light onlist-btn"> <i class="bx bx-plus label-icon"></i>Crea Nuovo</router-link>

                            </div>
                        </div>

                        <div class="table-responsive">
                            <table class="table table-bordered table-striped mb-0">

                                <thead class="table-dark">
                                    <tr>
                                        <th>RIF.</th>
                                        <th>Tipologia</th>
                                        <th>Stato</th>
                                        <th>Assegnato a</th>
                                        <th></th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="annuncio in annunci" v-bind:key="annuncio.id">
                                        <th scope="row">ERA-{{ annuncio.id}}</th>
                                        <td>{{ annuncio.type_immobile }}</td>
                                        <td>{{ annuncio.status }}</td>
                                        <td>
                                            <template v-if="annuncio.assigned_to">{{annuncio.assigned_to.username}}</template>
                                        </td>

                                        <td>
                                            <div class="dropdown">
                                                <a href="#" class="dropdown-toggle card-drop" data-bs-toggle="dropdown" aria-expanded="false">
                                                    <i class="mdi mdi-dots-horizontal font-size-18"></i>
                                                </a>
                                                <ul class="dropdown-menu dropdown-menu-end" style="">
                                                    <router-link class="dropdown-item" :to="{ name: 'Scheda_annuncio', params: { id: annuncio.id }}"><i class="mdi mdi-pencil font-size-16 text-success me-1"></i>Dettagli</router-link>
                                                    <li><a href="#" class="dropdown-item"><i class="mdi mdi-trash-can font-size-16 text-danger me-1"></i> Delete</a></li>
                                                </ul>
                                            </div>
                                        </td>
                                    </tr>

                                </tbody>
                            </table>
                        </div>

                    </div>
                </div>
            </div>
        </div>

    </div> <!-- container-fluid -->
</div>
<!-- End Page-content -->
<!--<div class="container page-container fade-in-load">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h1 class="title">Annunci</h1>

                 <router-link to="/dashboard/leads/add">Add annuncio</router-link> -->
<!-- </div>

            <div class="column is-12">
                <table class="table is-fullwidth">
                    <thead>
                        <tr>
                            <th>Rif.</th>
                            <th>Tipologia</th>
                            <th>Stato</th>
                            <th>Assegnato a </th>
                            <th></th>
                        </tr>
                    </thead>

                    <tbody>
                        <tr
                            v-for="annuncio in annunci"
                            v-bind:key="annuncio.id">
                                <td>ERA-{{ annuncio.id}}</td>
                                <td>{{ annuncio.type_immobile }}</td>
                                <td>{{ annuncio.status }}</td>
                                <td>
                                    <template v-if="annuncio.assigned_to">{{annuncio.assigned_to.username}}</template>
                                </td>
                                <td>
                                     <router-link :to="{ name: 'Scheda_annuncio', params: { id: annuncio.id }}">Details</router-link>
                                </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>-->
</template>

<script>
import axios from 'axios'

export default {
    name: 'Annunci',
    data() {
        return {
            annunci: []
        }
    },
    mounted() {
        this.getAnnunci()
    },
    methods: {
        async getAnnunci() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/annunci/')
                .then(response => {
                    this.annunci = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
