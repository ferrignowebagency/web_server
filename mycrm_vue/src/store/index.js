import { createStore } from 'vuex'

export default createStore({
    state: {
        isLoading: false,
        isAuthenticated: false,
        token: '',
        user: {
            id: 0,
            username: ''
        },
        agency: {
            id: 0,
            name: ''
        }
    },
    mutations: {
        initializeStore(state) {
            if (localStorage.getItem('token')) {
                state.token = localStorage.getItem('token')
                state.isAuthenticated = true
                state.user.username = localStorage.getItem('username')
                state.user.id = localStorage.getItem('userid')
                state.agency.name = localStorage.getItem('agency_name')
                state.agency.id = localStorage.getItem('agency_id')
            } else {
                state.token = ''
                state.isAuthenticated = false
                state.user.id = 0
                state.user.username = ''
                state.agency.id = 0
                state.agency.name = ''
            }
        },
        setIsLoading(state, status) {
            state.isLoading = status
        },
        setToken(state, token) {
            state.token = token
            state.isAuthenticated = true
        },
        removeToken(state) {
            state.token = ''
            state.isAuthenticated = false
        },
        setUser(state, user) {
            state.user = user
        },
        setAgency(state, agency) {
            state.agency = agency

            localStorage.setItem('agency_id', agency.id)
            localStorage.setItem('agency_name', agency.name)
        }
    },
    actions: {},
    modules: {}
})