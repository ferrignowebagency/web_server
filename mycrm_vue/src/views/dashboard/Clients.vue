<template>
<div class="page-content fade-in-load">
    <div class="container-fluid">

        <!-- start page title -->
        <div class="row">
            <div class="col-12">
                <div class="page-title-box d-sm-flex align-items-center justify-content-between">
                    <h4 class="mb-sm-0 font-size-18">Clienti</h4>

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
                                <b>Totale:</b> <span class="badge bg-primary easyre-badge" id="countTOTAL">{{ clients.length }}</span>
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
                                <tr v-for="client in clients" v-bind:key="client.id">
                                    <td>{{ client.type }}</td>
                                    <td>{{ client.name }} {{ client.surname }}</td>
                                    <td>{{ client.phone1 }}<br>{{ client.email }}</td>
                                    <td>
                                        <template v-if="client.assigned_to">{{client.assigned_to.username}}</template>
                                    </td>
                                    <td>
                                        <div class="dropdown">
                                            <a href="#" class="dropdown-toggle card-drop" data-bs-toggle="dropdown" aria-expanded="false">
                                                <i class="mdi mdi-dots-horizontal font-size-18"></i>
                                            </a>
                                            <ul class="dropdown-menu dropdown-menu-end" style="">
                                                <router-link class="dropdown-item" :to="{ name: 'Client_det', params: { id: client.id }}"><i class="bx bx-spreadsheet font-size-16 text-success me-1"></i>Scheda Cliente</router-link>
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
</div>
</div> <!-- container-fluid -->
</template>

<script>
import axios from 'axios'

export default {
    name: 'Clients',
    data() {
        return {
            clients: []
        }
    },
    mounted() {
        this.getClients()
    },
    methods: {
        async getClients() {
            this.$store.commit('setIsLoading', true)

            await axios
                .get('/api/v1/clients/')
                .then(response => {
                    this.clients = response.data
                })
                .catch(error => {
                    console.log(error)
                })
            
            this.$store.commit('setIsLoading', false)

        }

    }
}
</script>
