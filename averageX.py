var mapFunction1 = function() {
emit(this.userID, this.X);
};

var reduceFunction1 = function(userID, X) {
return Array.sum(X)/this.X;
};

db.transaction.mapReduce(
mapfunction1,
reduceFunction1,
{out:"mapreduce"}
)
