<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Agenti</h4>

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
        <h1 class="title">{{ agency.name }}</h1>
        <template v-if="agency.created_by.id === parseInt($store.state.user.id)">
            <router-link :to="{'name': 'add_agent'}" class="button is-primary">Add member</router-link>
        
        <div class="row">
            <div class="col-xl-12">
                <div class="card">
                    <div class="card-body">

                        <div class="d-flex justify-content-between align-items-center border-bottom text-uppercase" style="padding-top:0.75rem; padding-bottom:0.75rem;">
                            <div class="float-left">
                                <b>Totale:</b> <span class="badge bg-primary easyre-badge" id="countTOTAL">0</span>
                                <b>Filtrati:</b> <span class="badge bg-primary easyre-badge green" id="countFILTER">0</span>
                                <b>Selezionati:</b> <span class="badge bg-primary easyre-badge orange" id="countSELECT">22</span>
                            </div>
                            <div class="float-end">
                                <router-link to="/dashboard/annunci/add" type="button" class="btn btn-primary filter-btn btn-label waves-light onlist-btn"> <i class="bx bx-filter-alt label-icon"></i>Filtri</router-link>
                                <router-link to="/dashboard/clienti/add" type="button" class="btn btn-primary waves-effect btn-label waves-light onlist-btn"> <i class="bx bx-plus label-icon"></i>Crea Nuovo</router-link>
                            </div>
                        </div>
                        <div class="table-responsive">
                            <table class="table table-bordered table-striped mb-0">

                                <thead class="table-dark">
                                    <tr>
                                        <th>Tipo</th>
                                        <th>Nominativo</th>
                                        <th>Contatti</th>
                                        <th>Agente</th>
                                        <th></th>
                                    </tr>
                                </thead>

                                <tbody>
                                    <tr v-for="agent in agency.agents" v-bind:key="agent.id">
                                        <td>{{ agent.username }}</td>
                                        <td></td>
                                        <td></td>
                                        <td>

                                        </td>
                                        <td>
                                            <div class="dropdown">
                                                <a href="#" class="dropdown-toggle card-drop" data-bs-toggle="dropdown" aria-expanded="false">
                                                    <i class="mdi mdi-dots-horizontal font-size-18"></i>
                                                </a>
                                                <ul class="dropdown-menu dropdown-menu-end" style="">
                                                   <!-- <router-link class="dropdown-item" :to="{ name: 'Client_det', params: { id: client.id }}"><i class="bx bx-spreadsheet font-size-16 text-success me-1"></i>Scheda Cliente</router-link>-->
                                                    <li><a href="#" class="dropdown-item"><i class="mdi mdi-trash-can font-size-16 text-danger me-1"></i> Modifica</a></li>
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
        </template>
    </div>
</div>
</template>

<script>
import axios from 'axios'

export default {
    name: 'Agency',
    data() {
        return {
            agency: {
                agents: [],
                created_by: {}

            }
        }
    },
    mounted() {
        this.getAgency()
    },
    methods: {
        async getAgency() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/agency/get_my_agency/')
                .then(response => {
                    this.agency = response.data
                })
                .catch(error => {
                    console.log(error)
                })

            this.$store.commit('setIsLoading', false)
        }
    }
}
</script>
