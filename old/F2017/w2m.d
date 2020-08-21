import std.regex;
import std.bigint;

enum faculty_w2m_name = "Luther";

enum  pid = ctRegex!`PeopleIDs\[(\d+)\] = (\d+);`
	, pname = ctRegex!`PeopleNames\[(\d+)\] = '([^']*)';`
	, slot = ctRegex!`AvailableAtSlot\[(\d+)\].push\((\d+)\)`
	, tos = ctRegex!`TimeOfSlot\[(\d+)\]=(\d+);`
	, col = ctRegex!`Col\[TimeOfSlot.indexOf\((\d*)\)\] = (\d+);`
	, row = ctRegex!`Row\[TimeOfSlot.indexOf\((\d*)\)\] = (\d+);`
	, hexa = ctRegex!`// hexAvailability: ([0-9a-f]+)[\n\r]+AvailableAtSlot\[\d+\].push\((\d+)\);`
	, pnameid = ctRegex!`PeopleNames\[(\d+)\] = '([^']*)';PeopleIDs\[(\d+)\] = (\d+);`
	;

string[int] timeKey(string contents) {
	import std.datetime, std.conv;
	string[int] ans;
	foreach(m; contents.matchAll(tos)) {
		auto t = SysTime.fromUnixTime(to!long(m[2]), UTC());
		string tmp = text(t.dayOfWeek, " ", cast(TimeOfDay)t);
		ans[to!int(m[1])] = tmp[0..$-3];
	}
	return ans;
}

string[int] nameOf(string contents) {
	import std.conv;
	string[int] ans;
	foreach(m; contents.matchAll(pnameid)) {
		ans[to!int(m[4])] = m[2];
	}
	return ans;
}

BigInt[int] availabilityOf(string contents) {
	import std.conv;
	BigInt[int] ans;
	foreach(m; contents.matchAll(hexa)) {
		ans[to!int(m[2])] = BigInt("0x"~m[1]);
	}
	return ans;
}

BigInt[string] padTimes(BigInt[int] base, string[int] names, int padding) {
	BigInt[string] ans;
	foreach(k,v; base) {
		BigInt val = v;
		foreach(i; 0..padding) val &= (val << 1);
		ans[names[k]] = val;
	}
	return ans;
}

BigInt maxima(BigInt[string] base) {
	BigInt ans;
	foreach(k,v; base) ans |= v;
	return ans;
}

int delegate(int delegate(ref BigInt)) nBits(int maxPlace, int n, int gap=1) {
	BigInt one = 1;
	return (int delegate(ref BigInt) dg) {
		foreach_reverse(place; gap*(n-1) .. maxPlace+1) {
			BigInt num = one<<place;
			if (n > 1) {
				foreach(bi; nBits(place-gap, n-1, gap)) {
					BigInt tmp = bi | num;
					int result = dg(tmp);
					if (result != 0) return result;
				}
			} else {
				int result = dg(num);
				if (result != 0) return result;
			}
		}
		return 0;
	};
} 

string[] timesOfMask(BigInt mask, string[int] times) {
    string[] ans;
    int cnt = cast(int)(times.length - 1);
    for(BigInt ts = 1; ts <= mask && cnt >= 0; ts <<= 1, cnt -= 1)
		if ((ts & mask) != 0)
			ans ~= times[cnt];
    return ans;
}

string[] exceptions(BigInt times, BigInt[string] avail) {
	string[] ans;
	foreach(k,v; avail)
		if ((v & times) == 0)
			ans ~= k;
	return ans;
}

int[string] hoursListed(BigInt[string] avail) {
	int[string] ans;
	foreach(k,v; avail) {
		BigInt a = v;
		ans[k] = 0;
		while(a > 0) {
			if ((a&1) == 1) ans[k] += 1;
			a >>= 1;
		}
	}
	return ans;
}

void main(string[] args) {
	import std.stdio;
	static import std.file;
	
	if (args.length > 1) {
		import std.net.curl : download;
		download(args[1], "w2m.html");
	} else {
		writeln("No url given; using archived w2m.html");
	}

	auto s = cast(string)std.file.read("w2m.html");
	auto times = timeKey(s);
	auto avail = padTimes(availabilityOf(s), nameOf(s), 2);
	
	auto m = maxima(avail);
	
	int best = int.max;
	foreach(slots; 1..5) {
		writeln("\nChecking for ",slots," meeting time(s)");
		if (slots == 4) {
			int[string] hl = hoursListed(avail);
			foreach(k,v; hl) {
				if (v < 30) {
					writeln(k," listed just ",v);
					writeln("  ",timesOfMask(avail[k], times));
				}
			}
		}
		foreach(opt; nBits(cast(int)(m.uintLength*32), slots, 3)) {
			if ((opt & avail[faculty_w2m_name]) != opt) continue;
			int missed = 0;
			foreach(k,v; avail) {
				if (k == "Sarah Meng" || k == "Justin Choi" || k == "justincjchoi32") continue; // duplicate or all-false
				if ((v&opt) == 0) missed += 1;
				if (missed >= best) break;
			}
			if (missed < best) { 
				writefln("all but %d: %s %s", missed, timesOfMask(opt, times), exceptions(opt, avail));
				best = missed+1;
			}
		}
		best -= 1;
		if (best == 0) break;
	}
}
