import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import Home from '../views/Home.vue'

import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import Dashboard from '../views/dashboard/Dashboard.vue'
import MyAccount from '../views/dashboard/MyAccount.vue'
import Leads from '../views/dashboard/Leads.vue'
import Lead from '../views/dashboard/Lead.vue'
import AddLead from '../views/dashboard/AddLead.vue'
import EditLead from '../views/dashboard/EditLead.vue'
import Add_agency from '../views/dashboard/AddAgency.vue'
import Lista_agenzie from '../views/dashboard/Lista_agenzie.vue'
import add_agent from '../views/dashboard/Add_agent.vue'
import Edit_agent from '../views/dashboard/Edit_agent.vue'

// CLIENTI
import Clients from '../views/dashboard/Clients.vue'
import Add_client from '../views/dashboard/Add_client.vue'
import Client_det from '../views/dashboard/Scheda_cliente.vue'
import Client_edit from '../views/dashboard/Edit_Client.vue'
import Add_note from '../views/dashboard/Add_note.vue'
import Edit_note from '../views/dashboard/Edit_note.vue'

// ANNUNCI
import Lista_annunci from '../views/dashboard/Lista_annunci.vue'
import Scheda_annuncio from '../views/dashboard/Scheda_annuncio.vue'
import Edit_annuncio from '../views/dashboard/Edit_annuncio.vue'
import Add_annuncio from '../views/dashboard/Add_annuncio.vue'

// MISC
import NotFound from '../views/404.vue'


const routes = [{
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path: '/sign-up',
        name: 'SignUp',
        component: SignUp
    },
    {
        path: '/auth/login',
        name: 'LogIn',
        component: LogIn
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () =>
            import ( /* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/dashboard',
        name: 'Dashboard',
        component: Dashboard,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/my-account',
        name: 'MyAccount',
        component: MyAccount,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/leads',
        name: 'Leads',
        component: Leads,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/leads/add',
        name: 'AddLead',
        component: AddLead,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/leads/:id',
        name: 'Lead',
        component: Lead,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/leads/:id/edit',
        name: 'edit_lead',
        component: EditLead,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/add-agency',
        name: 'Add_agency',
        component: Add_agency,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/manager/lista-agenzie',
        name: 'lista_agenzie',
        component: Lista_agenzie,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/agencies/add_agent',
        name: 'add_agent',
        component: add_agent,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/agencies/edit-agent/:id/',
        name: 'Edit_agent',
        component: Edit_agent,
        meta: {
            requireLogin: true
        }
    },

    {
        path: '/dashboard/clienti',
        name: 'Clients',
        component: Clients,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/clienti/add',
        name: 'Add_client',
        component: Add_client,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/clienti/:id',
        name: 'Client_det',
        component: Client_det,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/clienti/:id/edit',
        name: 'Client_edit',
        component: Client_edit,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/clienti/:id/add-note',
        name: 'Add_note',
        component: Add_note,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/clienti/:id/edit-note',
        name: 'Edit_note',
        component: Edit_note,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/annunci/',
        name: 'Lista_annunci',
        component: Lista_annunci,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/annunci/scheda-annuncio/:id',
        name: 'Scheda_annuncio',
        component: Scheda_annuncio,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/annunci/scheda-annuncio/:id/edit',
        name: 'Edit_annuncio',
        component: Edit_annuncio,
        meta: {
            requireLogin: true
        }
    },
    {
        path: '/dashboard/annunci/add',
        name: 'Add_annuncio',
        component: Add_annuncio,
        meta: {
            requireLogin: true
        }
    },
    {
        path: "/:catchAll(.*)",
        name: "NotFound",
        component: NotFound,
    }




]


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
})

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
        next('/auth/login')
    } else {
        next()
    }
})

export default router