app.controller('loginController',function($scope,$http){
    $scope.user = {};
    $scope.login = function(){
    $scope.user.password = $scope.password;
    $scope.user.email = $scope.email;
    $http.post('http://localhost:8000/usuarios/login',$scope.user).success(function(msg){
            if(msg == "Logged User"){
                location.reload()
            }else{
                alert(msg)
            }
        })
    }
})