app.controller('TweetsSlider', ['$scope', '$http', '$interval', function($scope, $http, $interval){
	$scope.tweets = [];
	$scope.tweet = {};
	var i = 1;
	$http.get('http://jsonplaceholder.typicode.com/posts')
		.success(function(data){
			$scope.tweets = data;
			$scope.tweet = $scope.tweets[0];
		});
	$interval(function(){
		if(i == 2) i = 0;
		$scope.tweet = $scope.tweets[i];
		i++;
	}, 4000);
}]);