<template>
  <sidebar-menu @update:collapsed="onToggleCollapse" :menu="menu" />
</template>
<script>
  export default {
      data() {
          return {
              menu: [
                  {
                      header: false,
                      title: 'Dashboard',
                      hiddenOnCollapse: false,
                       href: '/dashboard',
                       icon:'bx bx-home-circle'
                  },
                  {
                      href: '/dashboard/annunci',
                      title: 'Annunci',
                      icon: 'bx bx-detail',
                      child: [
                          {
                              href: '/dashboard/annunci/add',
                              title: 'Nuovo'
                          }
                      ]
                  },
                  {
                      href: '/dashboard/leads',
                      title: 'Leads',
                      icon: 'fa fa-user'
                  },
                  {
                      href: '/dashboard/clienti',
                      title: 'Clienti',
                      icon: 'bx bx-user-check'
                  },
                  {
                      href: '/dashboard/leads',
                      title: 'Richieste',
                      icon: 'bx bx-user-plus'
                  },
                  {
                      href: '/dashboard/leads',
                      title: 'Incroci',
                      icon: 'bx bx-star'
                  },
                  {
                      href: '/none',
                      title: 'Agenda',
                      icon: 'bx bx-calendar',
                      child: [
                          {
                              href: '/2-1',
                              title: 'Menu 2-1'
                          }
                      ]
                  }
  
              ],  

              
          }
      },
      methods: {
        onToggleCollapse(collapsed) {
      return {
          minift:true
          }
        }
  }
  }
</script>

<style scoped>
.v-sidebar-menu {
    top: 70px!important;
}
.v-sidebar-menu.vsm_expanded {
    max-width: 250px!important;
}

.v-sidebar-menu {background: #2a3042;}
.v-sidebar-menu .vsm--toggle-btn {
    background-color: #2a3042!important;
    color: #fff;
}
.v-sidebar-menu i.vsm--icon {
    background-color: unset!important;
}
</style>