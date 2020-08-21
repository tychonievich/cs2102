import std.stdio, std.csv, std.file, std.conv, std.string, std.algorithm.searching, std.array;

ref T[] remove(T)(ref T[] array, T element) {
    int removed = 0;
    foreach(i; 0..array.length) {
        if (array[i] == element) removed += 1;
        else if (removed > 0) array[i-removed] = array[i];
    }
    array.length = array.length - removed;
    return array;
}

void main(string[] args) {
    if (args.length == 1) args ~= `optional.csv`;
    auto s = readText(args[1]);
    int seatCount = 5;
    int voteCount = 1;
    /* STV:
     * if have winning ratios of first-place votes
     *   then add to winners and a proportionally redistribute excess votes to second choice
     * if none have win, remove lowest-place candidate and redistribute votes
     * 
     * IRO:
     * remove least-ranked candidate and redistribute votes
     * repeat until just one candidate
     */
    string[][] votes;
    foreach(record; csvReader!(string[string])(s, null)) {
        if(`Timestamp` in record && record[`Timestamp`]) {
            string[] vote = new string[record.length - 1];
            foreach(k,v; record) {
                if (k.indexOf('[') < 0) continue;
                
                auto choice = k[k.indexOf('[')+1..k.lastIndexOf(']')];
                if (!v) continue;
                int p = to!int(v.length > 1 ? v[0..2].strip : v);
                vote[p-1] = choice;
            }
            votes ~= vote;
        }
    }
    while(votes[0].length > seatCount) {
        int max = int.min;
        string kill = "";
        foreach(option; votes[0]) {
            int dislike = 0;
            foreach(vote; votes) {
                if (!vote[0..seatCount].canFind(option)) dislike += 1;
            }
            if (dislike > max) { max = dislike; kill = option; }
        }
        foreach(ref vote; votes) {
            vote.remove(kill);
        }
    }
    writeln(votes[0]);
}
