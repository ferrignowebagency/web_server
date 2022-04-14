<template>
  <div>
    <h2>Your Address</h2>

    <vue-google-autocomplete
      ref="address"
      id="map"
      classname="form-control"
      placeholder="Inserisci l'indirizzo"
      v-on:placechanged="getAddressData"
      country="it"
      v-model="address"
    >
    </vue-google-autocomplete>
     <vue-google-autocomplete
      ref="city"
      id="map2"
      classname="form-control"
      placeholder="Inserisci l'indirizzo"
      v-on:placechanged="getCityData"
      country="it"
      v-model="locality"
    >
    </vue-google-autocomplete>

    <input v-model="locality" placeholder="Comune">
    <input v-model="province" placeholder="Provincia">
    <input v-model="regione" placeholder="Regione">
    <input v-model="zip_code" placeholder="Zip_code">
    <input v-model="latitude" placeholder="Latitude">
    <input v-model="longitude" placeholder="Longitude">
  </div>
</template>

<script>
  import VueGoogleAutocomplete from "vue-google-autocomplete";

  export default {
    components: { VueGoogleAutocomplete },

    data: function () {
      return {
        address: "",
        locality: "",
        province:"",
        regione:"",
        zip_code:"",
        latitude:"",
        longitude:"",
      };
    },

    mounted() {
      // To demonstrate functionality of exposed component functions
      // Here we make focus on the user input
      this.$refs.address.focus();
      this.$refs.city.focus();
    },

    methods: {
      /**
       * When the location found
       * @param {Object} addressData Data of the found location
       * @param {Object} placeResultData PlaceResult object
       * @param {String} id Input container ID
       */
      getAddressData: function (addressData, placeResultData, id) {
        this.address = addressData;
        console.log(addressData)
        
        
      }, 
      getCityData: function (addressData, placeResultData, id) {
        this.locality  = addressData.locality;
        this.province  = addressData.administrative_area_level_2;
        this.regione   = addressData.administrative_area_level_1;
        this.zip_code  = addressData.postal_code;
        this.latitude  = addressData.latitude;
        this.longitude = addressData.longitude;
        console.log(addressData)
    }
    },
  };
</script>