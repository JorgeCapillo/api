app.controller('registroController', ['$scope', '$http', function ($scope, $http) {
	//var divUserName = $('input[name = "userName"]').parentNode.nodeName;
	//$(divUserName).css({'background': 'red'});
	$scope.user = {};
	$scope.registro = function(){
		$scope.user.userName = $scope.userName;
		$scope.user.name = $scope.name;
		$scope.user.email = $scope.email;
		$scope.user.password = $scope.password;
		$http.post('http://localhost:8000/usuarios/crear', $scope.user )
			.success(function(msg){
				console.log(msg);
				if(msg == "Inavalid UserName"){
                    alert(msg)
					$('#conUserName').addClass('.has-error');
				}else if(msg == "Invalid Email"){
                    alert(msg)
					$('#email').addClass('.has-error');
				}else{
                    location.reload()
				}
					
			}).error(function(err){
				console.log(err);
			});
	};

}]);