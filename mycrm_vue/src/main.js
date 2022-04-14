import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'

import Popper from 'vue3-popper'
import "bootstrap"

// TOAST NOTIFICATION
import Toast from "vue-toastification";
import "vue-toastification/dist/index.css";

axios.defaults.baseURL = 'http://127.0.0.1:8000/'
import VueSidebarMenu from 'vue-sidebar-menu'
import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'

//import VueGoogleMaps from "@fawmi/vue-google-maps";




const options = {
    position: "bottom-right",
    timeout: 5000,
    closeOnClick: true,
    pauseOnFocusLoss: true,
    pauseOnHover: true,
    draggable: true,
    draggablePercent: 0.3,
    showCloseButtonOnHover: false,
    hideProgressBar: true,
    closeButton: "button",
    icon: true,
    rtl: false,
    transition: "Vue-Toastification__fade",
};
createApp(App)
    .use(store)
    .use(router, axios)
    .use(VueSidebarMenu)
    .use(Popper)
    .use(Toast, options)
    /*  .use(VueGoogleMaps, {
          load: {
              key: 'AIzaSyAdEWrvmC5SjqeLuKbHd89wZHTl8mSsi_4',
              language: 'it',
          },
      })*/

.mount('#app')