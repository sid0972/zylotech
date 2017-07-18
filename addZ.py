var mapFunction1 = function() {
emit(this.userID, this.Z);
};

var reduceFunction1 = function(userID, Z) {
return Array.sum(Z);
};

db.transaction.mapReduce(
mapfunction1,
reduceFunction1,
{out:"mapreduce"}
)
