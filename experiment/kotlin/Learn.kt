fun main(args: Array<String>){
val a  = IntArray(4)
val okay = indexOfMax(a)
println("$okay")
}
fun indexOfMax(a: IntArray): Int? {
	if (a == null)
		return null
    var keep: Int = 0
    for(tester in a){
		if(keep < tester)
    	keep = tester
	}
    return keep
}