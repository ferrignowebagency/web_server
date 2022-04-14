<template>
<div id="layout-wrapper">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" integrity="sha512-KfkfwYDsLkIlwQp6LFnl8zNdLGxu9YAA1QvwINks4PhcElQSvqcyVLLD9aMhXd13uQjoXtEKNosOWaZqXgel0g==" crossorigin="anonymous" referrerpolicy="no-referrer" />
    <template v-if="$store.state.isAuthenticated">
        <Navbar v-if="$route.path.includes('/dashboard') && $store.state.isAuthenticated" />
        <Sidebar v-if="$route.path.includes('/dashboard') && $store.state.isAuthenticated" />
        <div class="main-content" id="result">

        </div>

        <router-view />

        <Footer v-if="$route.path.includes('/dashboard') && $store.state.isAuthenticated" />
    </template>
    <template v-else>
        <div class="main-content" id="result">

        </div>

        <router-view />
    </template>

</div>
</template>

<script>
import axios from 'axios'

import Navbar from '@/components/layout/Navbar'
import Sidebar from '@/components/layout/Sidebar'
import Footer from '@/components/layout/Footer'

export default {
    name: 'App',
    components: {
        Navbar,
        Sidebar,
        Footer
    },
    beforeCreate() {
        this.$store.commit('initializeStore')

        if (this.$store.state.token) {
            axios.defaults.headers.common['Authorization'] = "Token " + this.$store.state.token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }

        if (!this.$store.state.agency.id) {
            this.$router.push('/dashboard/add-agency')
        }
    }

}
</script>

<style lang="scss">
//@import '../node_modules/bulma';

// Bootstrap Css
@import "../src/theme/css/bootstrap.min.css";
// Icons Css -->
@import "../src/theme/css/bootstrap.min.css";
@import "../src/theme/css/icons.min.css";

@import "../src/theme/css/app.min.css";
@import "../src/theme/css/main.css";
@import "../src/theme/css/custom.css";

@keyframes fadeIn {
    from {
        opacity: 0;
    }

    to {
        opacity: 1;
    }
}

.fade-in-load {
    opacity: 0;
    /* make things invisible upon start */
    animation: fadeIn ease-in 1;
    /* call our keyframe named fadeIn, use animattion ease-in and repeat it only 1 time */

    animation-fill-mode: forwards;
    /* this makes sure that after animation is done we remain at the last keyframe value (opacity: 1)*/

    animation-duration: 250ms;
    animation-delay: 0s
}

.lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
}

.lds-dual-ring:after {
    content: " ";
    display: block;
    width: 30px;
    height: 30px;
    margin: 8px;
    border-radius: 50%;
    border: 3px solid #fff;
    border-color: #fff transparent #ccc transparent;
    animation: lds-dual-ring 800ms linear infinite;
}

@keyframes lds-dual-ring {
    0% {
        transform: rotate(0deg);
    }

    100% {
        transform: rotate(360deg);
    }
}

.is-loading-bar {
    height: 0;
    overflow: hidden;
    top: 5px;
    position: relative;
    -webkit-transition: all 1s;
    transition: all 1s;

    &.is-loading {
        height: 55px;
    }
}

html,
body,
#app {
    height: 100%;
}

#app {
    min-height: 100%;
    //display: flex;
    //flex-direction: column;
}

.footer {
    margin-top: -12px;
}

@media screen and (max-width: 768px) {
    #menu-toggle:checked+.nav-menu {
        display: block;
    }
}

.columns {
    margin-top: 0px !important;
    margin-left: 0px !important;
    margin-right: 0px !important;
}

.page-container {
    background: #fafafa;
}

@media screen and (min-width: 1408px) {
    .container:not(.is-max-desktop):not(.is-max-widescreen) {
        max-width: 100%;
    }
}

@media screen and (min-width: 992px) {
    .page-content {
        margin-left: 250px;
    }
}

.easyre-badge {
    font-size: 100%;
    padding: 0.5em 0.7em !important;
    margin: 0px 0.4em;
}

.easyre-badge {
    background: #153b65 !important;
}

.easyre-badge.green {
    background: #2cab7d !important;
}

.easyre-badge.orange {
    background: #f1b44c !important;
}

.onlist-btn.btn-label .label-icon {
    background-color: #eff2f7;
}

.filter-btn {
    margin-right: 15px;
}

.onlist-btn {
    background: #fff;
    color: #153b65;
    border: 1px solid #ddd;
    font-weight: 500;
}

.onlist-btn:hover,
.onlist-btn:focus,
.onlist-btn:active {
    background: #f8f9fa;
    border: 1px solid #ddd;
    color: #153b65;
    box-shadow: unset;
}

.table-dark {
    --bs-table-bg: #153b65;
    --bs-table-striped-bg: #eff2f7;
    --bs-table-striped-color: #fff;
    --bs-table-active-bg: #484e53;
    --bs-table-active-color: #fff;
    --bs-table-hover-bg: #43494e;
    --bs-table-hover-color: #fff;
    color: #fff;
    border-color: #f6f6f6;
}

h6.card-title.mb-4 {
    padding: 15px 20px;
    background: #153b65;
    color: #fff;
}

.card-body.shadowed {

    background-color: #f8f9fa;
    box-shadow: rgb(0 0 0 / 2%) 0px 1px 3px 0px, rgb(27 31 35 / 15%) 0px 0px 0px 1px;

}

footer.footer.minift {
    left: 65px;
}

.vue-map {
    width: 100%;
    height: 100%;
    min-height: 362px;
}

@media screen and (min-width:1400px) {
    .container-fluid {
        max-width: 1500px;
    }

}

header.card-header.border-bottom.text-uppercase.text-white {
    display: inline-flex;
    justify-content: space-between;
    align-items: center;
}
</style>
