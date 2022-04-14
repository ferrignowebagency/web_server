<template>
        <footer class="footer" 
  :class="{ active: minift, 'text-danger': hasError }">
            <div class="container-fluid">
                <div class="row">
                    <div class="col-sm-6">
                         © Skote.
                    </div>
                    <div class="col-sm-6">
                        <div class="text-sm-end d-none d-sm-block">
                            Design & Develop by Themesbrand
                        </div>
                    </div>
                </div>
            </div>
        </footer>
    <!-- END layout-wrapper -->
</template>

<style scoped>
.footer {
    position: fixed;
}
</style>