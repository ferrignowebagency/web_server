<template>
<header id="page-topbar">
            <div class="navbar-header">
                <div class="d-flex">
                    <!-- LOGO -->
                    <div class="navbar-brand-box">
                        
                        <a href="dashboard" class="logo logo-light">
                              <span class="logo-sm">
                                <img src="https://export.easyre.srl/wp-content/themes/twenty-twenty-one-child/easyre-favicon.png" alt="" height="22">
                            </span>
                            <span class="logo-lg">
                                <img src="https://export.easyre.srl/wp-content/themes/twenty-twenty-one-child/logo-easyre-mini.png" alt="" height="17">
                            </span>
                        </a>
                    </div>

                    <button type="button" @update:collapsed="onToggleCollapse" class="btn btn-sm px-3 font-size-16 header-item waves-effect"
                        id="vertical-menu-btn">
                        <i class="fa fa-fw fa-bars"></i>
                    </button>

                    
                    
                </div>

                <div class="d-flex">

                    <div class="dropdown d-inline-block d-lg-none ms-2">
                        <button type="button" class="btn header-item noti-icon waves-effect"
                            id="page-header-search-dropdown" data-bs-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                            <i class="mdi mdi-magnify"></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0"
                            aria-labelledby="page-header-search-dropdown">

                            <form class="p-3">
                                <div class="form-group m-0">
                                    <div class="input-group">
                                        <input type="text" class="form-control" placeholder="Search ..."
                                            aria-label="Recipient's username">
                                        <div class="input-group-append">
                                            <button class="btn btn-primary" type="submit"><i
                                                    class="mdi mdi-magnify"></i></button>
                                        </div>
                                    </div>
                                </div>
                            </form>
                        </div>
                    </div>

                    

                    <div class="dropdown d-none d-lg-inline-block ms-1">
                        <button type="button" class="btn header-item noti-icon waves-effect" data-bs-toggle="dropdown"
                            aria-haspopup="true" aria-expanded="false">
                            <i class="bx bx-customize"></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-end">
                            <div class="px-lg-2">
                                <div class="row g-0">
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="/dashboard/annunci">
                                            <i style="font-size:25px;" class="bx bx-transfer-alt"></i>
                                            <span>Easysync</span>
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="/dashboard/annunci">
                                            <i style="font-size:25px;" class="bx bx-detail"></i>
                                            <span>Annunci</span>
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="/dashboard/annunci">
                                            <i style="font-size:25px;" class="bx bx-user-plus"></i>
                                            <span>Clienti</span>
                                        </a>
                                    </div>
                                </div>

                                <div class="row g-0">
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="#">
                                            <i style="font-size:25px;" class="bx bx-user-check"></i>
                                            <span>Richieste</span>
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="#">
                                            <i style="font-size:25px;" class="bx bx-star"></i>>
                                            <span>Incroci</span>
                                        </a>
                                    </div>
                                    <div class="col">
                                        <a class="dropdown-icon-item" href="#">
                                            <i style="font-size:25px;" class="bx bx-calendar"></i>
                                            <span>Agenda</span>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    

                    <div class="dropdown d-inline-block">
                        <button type="button" class="btn header-item noti-icon waves-effect"
                            id="page-header-notifications-dropdown" data-bs-toggle="dropdown" aria-haspopup="true"
                            aria-expanded="false">
                            <i class="bx bx-bell bx-tada"></i>
                            <span class="badge bg-danger rounded-pill">3</span>
                        </button>
                        <div class="dropdown-menu dropdown-menu-lg dropdown-menu-end p-0"
                            aria-labelledby="page-header-notifications-dropdown">
                            <div class="p-3">
                                <div class="row align-items-center">
                                    <div class="col">
                                        <h6 class="m-0" key="t-notifications"> Notifications </h6>
                                    </div>
                                    <div class="col-auto">
                                        <a href="#!" class="small" key="t-view-all"> View All</a>
                                    </div>
                                </div>
                            </div>
                            <div data-simplebar style="max-height: 230px;">
                                <a href="" class="text-reset notification-item">
                                    <div class="d-flex">
                                        <div class="avatar-xs me-3">
                                            <span class="avatar-title bg-primary rounded-circle font-size-16">
                                                <i class="bx bx-cart"></i>
                                            </span>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h6 class="mt-0 mb-1" key="t-your-order">Your order is placed</h6>
                                            <div class="font-size-12 text-muted">
                                                <p class="mb-1" key="t-grammer">If several languages coalesce the
                                                    grammar</p>
                                                <p class="mb-0"><i class="mdi mdi-clock-outline"></i> <span
                                                        key="t-min-ago">3 min ago</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </a>
                                <a href="" class="text-reset notification-item">
                                    <div class="d-flex">
                                        <img src="../../theme/images/users/avatar-3.jpg"
                                            class="me-3 rounded-circle avatar-xs" alt="user-pic">
                                        <div class="flex-grow-1">
                                            <h6 class="mt-0 mb-1">James Lemire</h6>
                                            <div class="font-size-12 text-muted">
                                                <p class="mb-1" key="t-simplified">It will seem like simplified English.
                                                </p>
                                                <p class="mb-0"><i class="mdi mdi-clock-outline"></i> <span
                                                        key="t-hours-ago">1 hours ago</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </a>
                                <a href="" class="text-reset notification-item">
                                    <div class="d-flex">
                                        <div class="avatar-xs me-3">
                                            <span class="avatar-title bg-success rounded-circle font-size-16">
                                                <i class="bx bx-badge-check"></i>
                                            </span>
                                        </div>
                                        <div class="flex-grow-1">
                                            <h6 class="mt-0 mb-1" key="t-shipped">Your item is shipped</h6>
                                            <div class="font-size-12 text-muted">
                                                <p class="mb-1" key="t-grammer">If several languages coalesce the
                                                    grammar</p>
                                                <p class="mb-0"><i class="mdi mdi-clock-outline"></i> <span
                                                        key="t-min-ago">3 min ago</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </a>

                                <a href="" class="text-reset notification-item">
                                    <div class="d-flex">
                                        <img src="../../theme/images/users/avatar-4.jpg"
                                            class="me-3 rounded-circle avatar-xs" alt="user-pic">
                                        <div class="flex-grow-1">
                                            <h6 class="mt-0 mb-1">Salena Layfield</h6>
                                            <div class="font-size-12 text-muted">
                                                <p class="mb-1" key="t-occidental">As a skeptical Cambridge friend of
                                                    mine occidental.</p>
                                                <p class="mb-0"><i class="mdi mdi-clock-outline"></i> <span
                                                        key="t-hours-ago">1 hours ago</span></p>
                                            </div>
                                        </div>
                                    </div>
                                </a>
                            </div>
                            <div class="p-2 border-top d-grid">
                                <a class="btn btn-sm btn-link font-size-14 text-center" href="javascript:void(0)">
                                    <i class="mdi mdi-arrow-right-circle me-1"></i> <span key="t-view-more">View
                                        More..</span>
                                </a>
                            </div>
                        </div>
                    </div>

                    <div class="dropdown d-inline-block">
                        <button type="button" class="btn header-item waves-effect" id="page-header-user-dropdown"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            <img class="rounded-circle header-profile-user" src="../../theme/images/users/avatar-1.jpg"
                                alt="Header Avatar">
                            <span class="d-none d-xl-inline-block ms-1" key="t-henry">{{user.first_name}}</span>
                            <i class="mdi mdi-chevron-down d-none d-xl-inline-block"></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-end">
                            <!-- item-->
                            <a class="dropdown-item" href="#"><i class="bx bx-user font-size-16 align-middle me-1"></i>
                                <span key="t-profile">Profile</span></a>
                            <a class="dropdown-item" href="#"><i
                                    class="bx bx-wallet font-size-16 align-middle me-1"></i> <span key="t-my-wallet">My
                                    Wallet</span></a>
                            <a class="dropdown-item d-block" href="#"><span
                                    class="badge bg-success float-end">11</span><i
                                    class="bx bx-wrench font-size-16 align-middle me-1"></i> <span
                                    key="t-settings">Settings</span></a>
                            <a class="dropdown-item" href="#"><i
                                    class="bx bx-lock-open font-size-16 align-middle me-1"></i> <span
                                    key="t-lock-screen">Lock screen</span></a>
                            <div class="dropdown-divider"></div>
                            <a class="dropdown-item text-danger" @click="logout()" href="javascript:void(0);"><i
                                    class="bx bx-power-off font-size-16 align-middle me-1 text-danger"></i> <span
                                    key="t-logout">Logout</span></a>
                        </div>
                    </div>

                    <div class="dropdown d-inline-block">
                        <button type="button" class="btn header-item noti-icon right-bar-toggle waves-effect" id="page-header-manager-dropdown"
                            data-bs-toggle="dropdown" aria-haspopup="true" aria-expanded="false"> 
                            <i class="bx bx-cog "></i>
                        </button>
                        <div class="dropdown-menu dropdown-menu-end">
                            <!-- item-->
                            <a class="dropdown-item" href="#"><i class="bx bx-user font-size-16 align-middle me-1"></i>
                                <span key="t-profile">Agenti</span></a>
            
                            <router-link class="dropdown-item" :to="{ name: 'lista_agenzie'}">
                                
                                <i class="bx bx-wrench font-size-16 align-middle me-1"></i><span>Agenzie</span></router-link>
                            <a class="dropdown-item" href="#"><i
                                    class="bx bx-lock-open font-size-16 align-middle me-1"></i> <span
                                    key="t-lock-screen">Lock screen</span></a>
                            <div class="dropdown-divider"></div>
                            {{userID}}
                        </div>
                    </div>

                </div>
            </div>
        </header>
</template>

<script>
    import axios from 'axios'
    export default {
        name: 'Navbar',
        data() {
        return {
            user: {},
            userID: {}
            }
            
        },
    mounted() {
       
        this.getUserID(),
        this.getUser()
        
    },
        methods: {            

            async getUserID() {
            //this.$store.commit('setIsLoading', true)
            
            //const userID = state.user.id
            await axios
                .get(`/api/v1/users/me/`)
                .then(response => {
                    this.userID = response.data.id
                   // console.log(response.data.id)                    
                })
                .catch(error => {
                    console.log(error)
                })
            
            
            //this.$store.commit('setIsLoading', false)
        }, 
            async getUser() {               

                const ID = this.userID
                console.log(ID)

                await axios
                    .get(`/api/v1/agency/agent/${ID}/`)
                    .then(response => {
                        this.user = response.data
                    })
                    .catch(error => {
                        console.log(error)
                    })

                
            },
        async logout() {
            await axios
                .post('/api/v1/token/logout/')
                .then(response => {
                    console.log('Logged out')
                })
                .catch(error => {
                    console.log(JSON.stringify(error))
                })

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            localStorage.removeItem('username')
            localStorage.removeItem('userid')
            localStorage.removeItem('agency_name')
            localStorage.removeItem('agency_id')
            this.$store.commit('removeToken')

            this.$router.push('/auth/login')
        }
    }
    }



</script>

<style scoped>
.navbar.is-white {
    padding: 0px 15px;
    box-shadow: rgb(9 30 66 / 5%) 0px 1px 42px 0px, rgb(9 30 66 / 8%) 0px 0px 0px 1px; 
}

body[data-sidebar=dark] .navbar-brand-box {
    background: #eff2f7;
}


</style>
