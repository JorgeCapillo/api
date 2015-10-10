var app = angular.module('signIn', []);

app.config(['$interpolateProvider', '$httpProvider',function ($interpolateProvider, $httpProvider) {
        //configuramos los símbolos  
         $interpolateProvider.startSymbol('[[');
         $interpolateProvider.endSymbol(']]');
         //configuramos el CSRFTOKEN para las peticiones con ANGULARJS
         $httpProvider.defaults.xsrfCookieName = 'csrftoken';
         $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
         $httpProvider.defaults.withCredentials = true;
         $httpProvider.defaults.cache=true;
         $httpProvider.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded;charset=utf-8';

         //función para compatibilidad de transmisión de datos JSON por POST

}]);