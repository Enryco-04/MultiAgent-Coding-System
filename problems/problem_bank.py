"""
problems/problem_bank.py
-------------------------
APPS benchmark problems adapted to Java + JUnit 5.
"""

PROBLEMS = [
        {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1579_E2. Array Optimization by Deque
        # Source  Original: Codeforces 1579E2 - Array Optimization by Deque

        # ──────────────────────────────────────────────────────────────────────
        "id": "minimum_instability_rail_log117",
        "title": "Minimum Instability Rail Loading",
        "class_name": "MinimumInstabilityRailLoading",

        "signature": "public static String solve(String input)",

        "description": """\
You are managing a two-way loading rail for a freight facility. For each schedule, containers arrive one by one in a fixed chronological sequence, each labeled with a specific weight parameter `w_i`.
You start with an initially empty linear rail.

When handling the arrival of `w_i`, you must attach it to the existing line of containers by either:
  - pushing it to the extreme front end, or
  - attaching it to the extreme rear end.

Once all containers are securely placed on the rail, an "instability metric" is evaluated for the finalized line.
This metric calculates the total number of positional pairs `(f, r)` satisfying:
  - `f < r` (meaning the container at position `f` sits closer to the front than the container at position `r`), and
  - the weight of the container at position `f` is strictly greater than the weight of the container at position `r`.

Your objective is to strategically route each sequentially arriving container to either the front or the rear to achieve the absolute lowest possible instability metric.

Input format:
  Line 1: t (number of test cases, 1 ≤ t ≤ 1000)
  For each test case:
    Line 1: n (1 ≤ n ≤ 2·10^5)
    Line 2: n space-separated integers w_i (-10^9 ≤ w_i ≤ 10^9)
  Sum of n over all test cases ≤ 2·10^5.

Output format:
  Print one integer per test case: the minimum achievable instability metric.

Implement full parsing and output formatting in `solve(String input)`.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MinimumInstabilityRailLoadingTest {

    private static String norm(String s) {
        if (s == null) return "";
        s = s.replace("\\r\\n", "\\n").replace("\\r", "\\n");
        String[] lines = s.split("\\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            int end = line.length();
            while (end > 0 && Character.isWhitespace(line.charAt(end - 1))) end--;
            sb.append(line, 0, end).append('\\n');
        }
        return sb.toString().trim();
    }

    private void assertCase(String input, String expected) {
        String actual = MinimumInstabilityRailLoading.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    // ── official example ──────────────────────────────────────────────────────

    @Test void case00() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }

    // ── single-element arrays always give 0 inversions ────────────────────────

    @Test void case01() { assertCase("1\\n1\\n-1000000000\\n", "0\\n"); }
    @Test void case03() { assertCase("1\\n1\\n-1090552905\\n", "0\\n"); }
    @Test void case71() { assertCase("1\\n1\\n-1572755758\\n", "0\\n"); }
    @Test void case72() { assertCase("1\\n1\\n-1994447814\\n", "0\\n"); }
    @Test void case77() { assertCase("1\\n1\\n-3557835192\\n", "0\\n"); }
    @Test void case81() { assertCase("1\\n1\\n-1177154308\\n", "0\\n"); }
    @Test void case85() { assertCase("1\\n1\\n-404786817\\n", "0\\n"); }
    @Test void case86() { assertCase("1\\n1\\n-2306668450\\n", "0\\n"); }
    @Test void case88() { assertCase("1\\n1\\n-170211275\\n", "0\\n"); }
    @Test void case101() { assertCase("1\\n1\\n-41790379\\n", "0\\n"); }
    @Test void case149() { assertCase("1\\n1\\n-1182291871\\n", "0\\n"); }
    @Test void case152() { assertCase("1\\n1\\n-2072621836\\n", "0\\n"); }
    @Test void case156() { assertCase("1\\n1\\n-2060860677\\n", "0\\n"); }
    @Test void case161() { assertCase("1\\n1\\n-5490202626\\n", "0\\n"); }
    @Test void case164() { assertCase("1\\n1\\n-303186913\\n", "0\\n"); }
    @Test void case167() { assertCase("1\\n1\\n-335830449\\n", "0\\n"); }
    @Test void case170() { assertCase("1\\n1\\n-2980236549\\n", "0\\n"); }
    @Test void case171() { assertCase("1\\n1\\n-137484530\\n", "0\\n"); }

    // ── n=5, large values ─────────────────────────────────────────────────────

    @Test void case02() { assertCase("1\\n5\\n999999996 999999997 1000000000 999999998 999999999\\n", "2\\n"); }
    @Test void case05() { assertCase("1\\n5\\n999999996 594621428 1000000000 999999998 999999999\\n", "2\\n"); }
    @Test void case07() { assertCase("1\\n5\\n999999996 999999997 1000000000 714491994 999999999\\n", "1\\n"); }
    @Test void case30() { assertCase("1\\n5\\n1952608156 755572301 1101000000 999999998 999999999\\n", "4\\n"); }
    @Test void case31() { assertCase("1\\n5\\n1281844869 594621428 1000000000 1496043289 1013691690\\n", "3\\n"); }
    @Test void case75() { assertCase("1\\n5\\n999999996 594621428 1001000000 999999998 999999999\\n", "2\\n"); }
    @Test void case80() { assertCase("1\\n5\\n999999996 755572301 1001000000 999999998 999999999\\n", "2\\n"); }
    @Test void case87() { assertCase("1\\n5\\n999999996 594621428 1000000000 1496043289 999999999\\n", "2\\n"); }
    @Test void case90() { assertCase("1\\n5\\n999999996 594621428 1001000000 628405048 999999999\\n", "2\\n"); }
    @Test void case94() { assertCase("1\\n5\\n999999996 755572301 1101000000 999999998 999999999\\n", "2\\n"); }
    @Test void case97() { assertCase("1\\n5\\n999999996 999999997 1000000000 1318373358 999999999\\n", "2\\n"); }
    @Test void case100() { assertCase("1\\n5\\n1281844869 594621428 1000000000 1496043289 999999999\\n", "2\\n"); }
    @Test void case103() { assertCase("1\\n5\\n999999996 256091627 1001000000 628405048 999999999\\n", "2\\n"); }
    @Test void case105() { assertCase("1\\n5\\n999999996 755572301 1101000000 999999998 1368676000\\n", "1\\n"); }
    @Test void case107() { assertCase("1\\n5\\n999999996 999999997 1001000000 1318373358 999999999\\n", "2\\n"); }
    @Test void case109() { assertCase("1\\n5\\n236424498 594621428 1000000000 1496043289 999999999\\n", "2\\n"); }
    @Test void case110() { assertCase("1\\n5\\n999999996 256091627 1001000000 628405048 1063115534\\n", "1\\n"); }
    @Test void case113() { assertCase("1\\n5\\n999999996 755572301 0101000000 999999998 1368676000\\n", "0\\n"); }
    @Test void case116() { assertCase("1\\n5\\n236424498 594621428 1010000000 1496043289 999999999\\n", "2\\n"); }
    @Test void case118() { assertCase("1\\n5\\n999999996 256091627 1001000000 330631407 1063115534\\n", "1\\n"); }
    @Test void case121() { assertCase("1\\n5\\n999999996 755572301 0101000000 733198157 1368676000\\n", "1\\n"); }
    @Test void case124() { assertCase("1\\n5\\n236424498 842458350 1010000000 1496043289 999999999\\n", "2\\n"); }
    @Test void case125() { assertCase("1\\n5\\n875031871 256091627 1001000000 330631407 1063115534\\n", "1\\n"); }
    @Test void case127() { assertCase("1\\n5\\n999999996 755572301 0101000000 90693554 1368676000\\n", "0\\n"); }
    @Test void case130() { assertCase("1\\n5\\n236424498 842458350 1010100000 1496043289 999999999\\n", "2\\n"); }
    @Test void case132() { assertCase("1\\n5\\n999999996 109225457 0101000000 90693554 1368676000\\n", "0\\n"); }
    @Test void case135() { assertCase("1\\n5\\n236424498 842458350 1000100000 1496043289 999999999\\n", "2\\n"); }
    @Test void case138() { assertCase("1\\n5\\n999999996 109225457 0101000000 138689760 1368676000\\n", "1\\n"); }
    @Test void case141() { assertCase("1\\n5\\n999999996 26547904 0101000000 138689760 1368676000\\n", "2\\n"); }
    @Test void case145() { assertCase("1\\n5\\n999999996 26547904 0101100000 138689760 1368676000\\n", "2\\n"); }
    @Test void case147() { assertCase("1\\n5\\n999999996 26547904 0101100010 138689760 1368676000\\n", "2\\n"); }
    @Test void case150() { assertCase("1\\n5\\n999999996 999999997 1000000000 999999998 1212312430\\n", "1\\n"); }
    @Test void case155() { assertCase("1\\n5\\n999999996 594621428 1000000000 999999998 1844965305\\n", "1\\n"); }
    @Test void case159() { assertCase("1\\n5\\n999999996 594621428 1001000000 1449709188 999999999\\n", "2\\n"); }
    @Test void case163() { assertCase("1\\n5\\n912921884 755572301 1001000000 999999998 999999999\\n", "2\\n"); }
    @Test void case172() { assertCase("1\\n5\\n999999996 472578341 1001000000 628405048 999999999\\n", "2\\n"); }
    @Test void case175() { assertCase("1\\n5\\n999999996 999999997 1000000100 1318373358 999999999\\n", "2\\n"); }
    @Test void case179() { assertCase("1\\n5\\n999999996 256091627 1001000000 628405048 1112913869\\n", "1\\n"); }
    @Test void case183() { assertCase("1\\n5\\n1009392756 755572301 1101000000 999999998 1368676000\\n", "1\\n"); }
    @Test void case186() { assertCase("1\\n5\\n999999996 999999997 1001000000 1318373358 195849909\\n", "0\\n"); }
    @Test void case188() { assertCase("1\\n5\\n236424498 594621428 1000100000 1496043289 999999999\\n", "2\\n"); }
    @Test void case190() { assertCase("1\\n5\\n999999996 14187850 1001000000 628405048 1063115534\\n", "1\\n"); }
    @Test void case193() { assertCase("1\\n5\\n999999996 755572301 0101000000 999999998 1770800587\\n", "0\\n"); }
    @Test void case195() { assertCase("1\\n5\\n236424498 594621428 1010001000 1496043289 999999999\\n", "2\\n"); }
    @Test void case196() { assertCase("1\\n5\\n999999996 256091627 0001000000 330631407 1063115534\\n", "1\\n"); }
    @Test void case198() { assertCase("1\\n5\\n999999996 755572301 0101000000 407201525 1368676000\\n", "1\\n"); }
    @Test void case200() { assertCase("1\\n5\\n236424498 842458350 1010000000 1496043289 1990754\\n", "0\\n"); }
    @Test void case202() { assertCase("1\\n5\\n875031871 256091627 1001000000 219086351 1063115534\\n", "0\\n"); }

    // ── 6-case batches ────────────────────────────────────────────────────────

    @Test void case04() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case06() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 4 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case08() { assertCase("6\\n4\\n3 0 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case09() { assertCase("6\\n4\\n3 7 5 1\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case10() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case11() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n1\\n1\\n2\\n"); }
    @Test void case12() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n0 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case13() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case14() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 0\\n", "2\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case15() { assertCase("6\\n4\\n3 0 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -2\\n4\\n4 5 1 3\\n5\\n2 3 1 3 1\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case16() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n4 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case17() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 2 2\\n4\\n-1 2 1 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case18() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "1\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case19() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n1 3 0 4 2\\n", "1\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case20() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n2 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case21() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n2 5 1 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case22() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n0 5 1 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n2\\n2\\n"); }
    @Test void case23() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 3 2 3\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n2\\n1\\n2\\n"); }
    @Test void case24() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 3 2 3\\n5\\n1 3 0 8 1\\n", "1\\n0\\n0\\n2\\n1\\n1\\n"); }
    @Test void case25() { assertCase("6\\n4\\n3 1 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 3 2 3\\n5\\n1 3 0 8 1\\n", "0\\n0\\n0\\n2\\n1\\n1\\n"); }
    @Test void case26() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -2\\n4\\n0 5 1 3\\n5\\n2 3 0 2 0\\n", "0\\n0\\n0\\n1\\n2\\n1\\n"); }
    @Test void case27() { assertCase("6\\n4\\n3 1 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 3 2 3\\n5\\n1 3 1 8 1\\n", "0\\n0\\n0\\n2\\n1\\n0\\n"); }
    @Test void case28() { assertCase("6\\n4\\n3 1 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 2 0\\n4\\n4 3 2 3\\n5\\n1 3 1 8 1\\n", "0\\n0\\n0\\n1\\n1\\n0\\n"); }
    @Test void case29() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 0 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n2\\n1\\n"); }
    @Test void case32() { assertCase("6\\n4\\n5 7 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-2 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 0\\n", "0\\n0\\n1\\n1\\n1\\n0\\n"); }
    @Test void case33() { assertCase("6\\n4\\n3 0 4 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -2\\n4\\n4 5 1 5\\n5\\n2 3 1 3 1\\n", "0\\n0\\n1\\n0\\n0\\n0\\n"); }
    @Test void case34() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 2 6\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n1\\n0\\n2\\n"); }
    @Test void case35() { assertCase("6\\n4\\n7 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 4 2 4\\n5\\n1 3 0 4 0\\n", "2\\n0\\n1\\n0\\n0\\n0\\n"); }
    @Test void case36() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 3 2 0\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n2\\n0\\n2\\n"); }
    @Test void case37() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -2\\n4\\n0 5 1 3\\n5\\n2 2 0 2 2\\n", "0\\n0\\n0\\n1\\n2\\n0\\n"); }
    @Test void case38() { assertCase("6\\n4\\n6 7 5 1\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 0 1 4 2\\n", "0\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case39() { assertCase("6\\n4\\n2 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 0\\n", "1\\n0\\n0\\n1\\n1\\n0\\n"); }
    @Test void case40() { assertCase("6\\n4\\n3 0 4 5\\n3\\n3 2 1\\n3\\n3 1 4\\n4\\n-1 2 2 -1\\n4\\n4 5 1 2\\n5\\n2 3 1 3 1\\n", "0\\n0\\n0\\n0\\n1\\n0\\n"); }
    @Test void case41() { assertCase("6\\n4\\n5 3 5 5\\n3\\n3 0 1\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 4 2 3\\n5\\n0 3 0 4 0\\n", "0\\n1\\n1\\n0\\n1\\n0\\n"); }
    @Test void case42() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 1 2\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 2 1 3\\n5\\n2 3 0 4 2\\n", "2\\n1\\n1\\n0\\n1\\n1\\n"); }
    @Test void case43() { assertCase("6\\n4\\n5 1 5 7\\n3\\n3 3 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 1 2 3\\n5\\n1 3 1 8 1\\n", "0\\n0\\n0\\n2\\n2\\n0\\n"); }
    @Test void case44() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n5 5 1 3\\n5\\n4 1 1 4 2\\n", "2\\n1\\n1\\n0\\n1\\n2\\n"); }
    @Test void case45() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 1 2\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 2 1 3\\n5\\n2 3 0 4 0\\n", "2\\n1\\n1\\n0\\n1\\n0\\n"); }
    @Test void case46() { assertCase("6\\n4\\n3 7 4 10\\n3\\n1 2 1\\n3\\n3 1 2\\n4\\n-1 2 1 -2\\n4\\n7 5 1 3\\n5\\n2 3 0 4 2\\n", "1\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case47() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n2 1 1 3\\n5\\n2 3 0 3 4\\n", "0\\n0\\n0\\n1\\n0\\n0\\n"); }
    @Test void case48() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 -1 -1\\n4\\n4 3 3 6\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n0\\n0\\n2\\n"); }
    @Test void case49() { assertCase("6\\n4\\n5 1 3 7\\n3\\n3 3 0\\n3\\n1 1 2\\n4\\n-1 2 1 0\\n4\\n4 1 2 3\\n5\\n1 3 1 8 1\\n", "1\\n0\\n0\\n2\\n2\\n0\\n"); }
    @Test void case50() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n0 5 2 3\\n5\\n1 3 2 1 2\\n", "2\\n0\\n1\\n0\\n2\\n2\\n"); }
    @Test void case51() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 2 -1\\n4\\n0 5 2 3\\n5\\n1 3 2 1 2\\n", "2\\n0\\n0\\n0\\n2\\n2\\n"); }
    @Test void case52() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 1 2\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n2 2 1 3\\n5\\n2 3 0 5 0\\n", "2\\n1\\n1\\n0\\n0\\n0\\n"); }
    @Test void case53() { assertCase("6\\n4\\n3 7 5 4\\n3\\n3 5 1\\n3\\n3 5 2\\n4\\n-1 2 1 -1\\n4\\n4 1 1 3\\n5\\n1 3 1 0 3\\n", "2\\n0\\n0\\n1\\n1\\n0\\n"); }
    @Test void case54() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 1\\n3\\n3 1 2\\n4\\n-1 2 0 -1\\n4\\n6 5 1 3\\n5\\n4 1 1 0 2\\n", "2\\n1\\n1\\n1\\n1\\n1\\n"); }
    @Test void case55() { assertCase("6\\n4\\n3 7 7 5\\n3\\n3 1 2\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n2 2 1 3\\n5\\n2 3 0 5 0\\n", "1\\n1\\n1\\n0\\n0\\n0\\n"); }
    @Test void case56() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n6 1 0\\n4\\n-1 2 2 0\\n4\\n0 5 2 3\\n5\\n1 3 2 1 2\\n", "2\\n0\\n0\\n1\\n2\\n2\\n"); }
    @Test void case57() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 1\\n3\\n6 1 0\\n4\\n-1 2 2 0\\n4\\n0 5 2 3\\n5\\n1 3 2 1 2\\n", "2\\n1\\n0\\n1\\n2\\n2\\n"); }
    @Test void case58() { assertCase("6\\n4\\n3 7 8 15\\n3\\n3 2 1\\n3\\n3 0 0\\n4\\n-1 2 1 -1\\n4\\n2 1 1 3\\n5\\n2 4 -1 3 5\\n", "0\\n0\\n0\\n1\\n0\\n1\\n"); }
    @Test void case59() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 1\\n3\\n6 1 0\\n4\\n-1 2 2 0\\n4\\n0 5 2 3\\n5\\n1 3 2 1 3\\n", "2\\n1\\n0\\n1\\n2\\n1\\n"); }
    @Test void case60() { assertCase("6\\n4\\n3 7 8 15\\n3\\n3 2 1\\n3\\n3 0 0\\n4\\n-1 2 1 0\\n4\\n2 1 1 3\\n5\\n2 4 -1 3 5\\n", "0\\n0\\n0\\n2\\n0\\n1\\n"); }
    @Test void case61() { assertCase("6\\n4\\n3 7 8 15\\n3\\n3 2 1\\n3\\n3 0 0\\n4\\n-1 2 1 0\\n4\\n2 1 1 3\\n5\\n2 4 -1 3 1\\n", "0\\n0\\n0\\n2\\n0\\n2\\n"); }
    @Test void case62() { assertCase("6\\n4\\n2 11 5 0\\n3\\n5 5 1\\n3\\n3 5 2\\n4\\n-1 2 1 -1\\n4\\n4 0 1 3\\n5\\n1 3 1 0 5\\n", "1\\n0\\n0\\n1\\n2\\n0\\n"); }
    @Test void case63() { assertCase("6\\n4\\n3 7 8 15\\n3\\n3 2 1\\n3\\n3 0 0\\n4\\n-1 2 1 0\\n4\\n4 1 1 3\\n5\\n2 4 -1 3 1\\n", "0\\n0\\n0\\n2\\n1\\n2\\n"); }
    @Test void case64() { assertCase("6\\n4\\n2 11 8 0\\n3\\n10 2 1\\n3\\n3 5 2\\n4\\n1 2 1 -1\\n4\\n4 0 1 6\\n5\\n1 5 1 0 0\\n", "1\\n0\\n0\\n0\\n1\\n0\\n"); }
    @Test void case65() { assertCase("6\\n4\\n2 11 8 -1\\n3\\n10 2 1\\n3\\n3 10 2\\n4\\n1 2 1 -1\\n4\\n4 0 1 6\\n5\\n1 5 1 -1 0\\n", "1\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case66() { assertCase("6\\n4\\n2 11 8 -1\\n3\\n10 2 1\\n3\\n5 10 2\\n4\\n1 2 1 -1\\n4\\n1 0 1 6\\n5\\n1 5 1 -1 0\\n", "1\\n0\\n0\\n0\\n0\\n1\\n"); }
    @Test void case67() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n1 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n0\\n0\\n1\\n2\\n"); }
    @Test void case68() { assertCase("6\\n4\\n3 7 5 1\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n0 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n3\\n"); }
    @Test void case69() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 4\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n1\\n0\\n1\\n"); }
    @Test void case70() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case73() { assertCase("6\\n4\\n3 7 6 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case74() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case76() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 4 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case78() { assertCase("6\\n4\\n3 7 6 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case79() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case82() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case83() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case84() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case89() { assertCase("6\\n4\\n3 7 8 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 0 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case91() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case92() { assertCase("6\\n4\\n3 7 6 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 2 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case93() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case95() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-1 2 2 -1\\n4\\n8 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case96() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case98() { assertCase("6\\n4\\n3 0 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -2\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case99() { assertCase("6\\n4\\n3 7 5 1\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case102() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case104() { assertCase("6\\n4\\n3 7 6 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n-1 2 3 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 2 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case106() { assertCase("6\\n4\\n3 7 5 4\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-1 2 2 -1\\n4\\n8 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case108() { assertCase("6\\n4\\n3 7 5 1\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n3 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case111() { assertCase("6\\n4\\n3 7 6 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n-1 2 3 -1\\n4\\n7 5 1 3\\n5\\n2 3 1 2 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case112() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n0 2 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case114() { assertCase("6\\n4\\n5 7 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 0\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case115() { assertCase("6\\n4\\n3 0 4 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -2\\n4\\n4 5 1 3\\n5\\n2 3 1 3 1\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case117() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n2 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case119() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n2 2 2\\n4\\n-1 2 1 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case120() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n0 2 2\\n4\\n-1 2 0 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case122() { assertCase("6\\n4\\n5 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 0\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case123() { assertCase("6\\n4\\n3 0 4 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 1\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case126() { assertCase("6\\n4\\n3 13 5 4\\n3\\n3 2 1\\n3\\n0 2 2\\n4\\n-1 2 0 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case128() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 0 -1\\n4\\n4 3 1 3\\n5\\n1 3 0 4 2\\n", "1\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case129() { assertCase("6\\n4\\n5 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n1 3 0 4 0\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case131() { assertCase("6\\n4\\n3 13 5 4\\n3\\n3 2 1\\n3\\n0 2 0\\n4\\n-1 2 0 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case133() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 0 -1\\n4\\n4 3 2 3\\n5\\n1 3 0 4 2\\n", "1\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case134() { assertCase("6\\n4\\n5 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 2 3\\n5\\n1 3 0 4 0\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case136() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n2 5 1 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case137() { assertCase("6\\n4\\n3 13 5 4\\n3\\n3 2 0\\n3\\n0 2 0\\n4\\n-1 2 0 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case139() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 0 -1\\n4\\n4 3 2 3\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case140() { assertCase("6\\n4\\n5 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 4 2 3\\n5\\n1 3 0 4 0\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case142() { assertCase("6\\n4\\n3 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 2 3\\n5\\n1 3 0 8 2\\n", "1\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case143() { assertCase("6\\n4\\n7 3 5 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 4 2 3\\n5\\n1 3 0 4 0\\n", "2\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case144() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n0 5 0 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case146() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -2\\n4\\n0 5 0 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case148() { assertCase("6\\n4\\n3 7 8 1\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -2\\n4\\n0 5 1 3\\n5\\n2 3 0 2 2\\n", "0\\n0\\n0\\n1\\n2\\n2\\n"); }
    @Test void case151() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n1 3 1 1 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case153() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 1 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case154() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n5 5 1 3\\n5\\n2 3 1 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case157() { assertCase("6\\n4\\n3 7 6 5\\n3\\n3 2 1\\n3\\n3 2 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "2\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case158() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 2 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case160() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 4 1\\n3\\n3 1 2\\n4\\n-1 2 2 -2\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case162() { assertCase("6\\n4\\n3 7 5 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case165() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 -1 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case166() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 2 0\\n3\\n6 1 2\\n4\\n-2 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case168() { assertCase("6\\n4\\n3 0 5 5\\n3\\n3 3 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case169() { assertCase("6\\n4\\n3 7 5 1\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n6 5 1 3\\n5\\n2 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case173() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 14 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case174() { assertCase("6\\n4\\n3 7 1 5\\n3\\n3 0 0\\n3\\n6 1 2\\n4\\n-1 2 3 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case176() { assertCase("6\\n4\\n3 0 5 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 4 -2\\n4\\n4 5 1 3\\n5\\n2 3 1 3 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case177() { assertCase("6\\n4\\n6 7 5 1\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 4 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case178() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 1 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case180() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n4 5 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n1\\n1\\n1\\n2\\n"); }
    @Test void case181() { assertCase("6\\n4\\n3 7 6 5\\n3\\n6 2 1\\n3\\n3 1 2\\n4\\n0 2 3 -1\\n4\\n4 5 1 3\\n5\\n2 3 1 2 2\\n", "2\\n0\\n1\\n0\\n1\\n2\\n"); }
    @Test void case182() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n0 2 2\\n4\\n-1 2 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 -1 4 2\\n", "2\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case184() { assertCase("6\\n4\\n3 7 4 5\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case185() { assertCase("6\\n4\\n3 7 5 4\\n3\\n3 2 0\\n3\\n10 1 2\\n4\\n-1 2 2 -1\\n4\\n8 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case187() { assertCase("6\\n4\\n3 8 5 1\\n3\\n3 2 0\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 3\\n5\\n3 3 1 4 2\\n", "1\\n0\\n1\\n0\\n1\\n1\\n"); }
    @Test void case189() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 1 -1\\n4\\n7 5 1 3\\n5\\n2 3 0 4 2\\n", "0\\n0\\n1\\n1\\n1\\n1\\n"); }
    @Test void case191() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n3 3 2\\n4\\n-1 2 1 -1\\n4\\n4 7 1 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case192() { assertCase("6\\n4\\n3 13 5 5\\n3\\n3 2 1\\n3\\n0 2 2\\n4\\n-1 0 2 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "2\\n0\\n0\\n0\\n1\\n1\\n"); }
    @Test void case194() { assertCase("6\\n4\\n2 7 5 7\\n3\\n3 2 0\\n3\\n1 1 2\\n4\\n-1 2 1 -1\\n4\\n4 3 1 3\\n5\\n2 3 0 4 2\\n", "1\\n0\\n0\\n1\\n1\\n1\\n"); }
    @Test void case197() { assertCase("6\\n4\\n3 7 5 5\\n3\\n3 5 1\\n3\\n2 2 2\\n4\\n-1 2 1 -1\\n4\\n4 7 2 3\\n5\\n1 3 1 3 2\\n", "2\\n0\\n0\\n1\\n1\\n2\\n"); }
    @Test void case199() { assertCase("6\\n4\\n3 0 4 5\\n3\\n3 2 1\\n3\\n3 1 2\\n4\\n-1 2 2 -1\\n4\\n4 5 1 2\\n5\\n2 3 1 3 1\\n", "0\\n0\\n1\\n0\\n1\\n0\\n"); }
    @Test void case201() { assertCase("6\\n4\\n3 7 8 10\\n3\\n3 2 1\\n3\\n3 1 0\\n4\\n-1 2 1 -1\\n4\\n2 5 1 3\\n5\\n2 3 0 4 4\\n", "0\\n0\\n0\\n1\\n1\\n0\\n"); }
}
""",
    },
    # ----------------------------------------------------------------------
    # ──────────────────────────────────────────────────────────────────────
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    
    #{
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Relay Window Shift Planning
        #Source CodeForces 949C 

#        # ──────────────────────────────────────────────────────────────────────
#        "id": "relay_window_shift",
#        "title": "Relay Window Shift Planning",
#        "class_name": "RelayWindowShift",
#
#        "signature": "public static int minRelaysToShift(int n, int cycleLength, int[] offlineSlot, int[][] mirroredPairs)",
#
#        "description": """\
#A distributed relay network has `n` relays, indexed 1..n.

#Each relay is briefly offline once per cycle of `cycleLength` slots.
#Relay `j` is offline during slot `offlineSlot[j-1]` (0-based).

#Each payload is mirrored on exactly two relays. If those two relays are
#offline in the same slot, that payload becomes unavailable.
#The given schedule is initially safe.

#Engineers want to run an experiment:
#- choose a non-empty subset of relays;
#- shift each chosen relay's offline slot forward by exactly 1 (mod cycleLength).

#After the shift, the schedule must still be safe for every mirrored pair.

#Return the minimum possible number of chosen relays.

#Input notes:
#- Each `mirroredPairs[i]` has form `[a, b]` with 1-based indices and `a != b`.

#Constraints:
#- 2 <= n <= 100000
#- 1 <= mirroredPairs.length <= 100000
#- 2 <= cycleLength <= 100000
#- 0 <= offlineSlot[j] < cycleLength
#- Initial schedule is valid for all pairs.
#""",
#
#        "junit_test": """\
#import org.junit.jupiter.api.Test;
#import static org.junit.jupiter.api.Assertions.*;
#import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
#import java.time.Duration;

#class RelayWindowShiftTest {

#    private int bruteMin(int n, int h, int[] u, int[][] pairs) {
#        int best = Integer.MAX_VALUE;
#        int totalMasks = 1 << n;
#        for (int mask = 1; mask < totalMasks; mask++) {
#            if (Integer.bitCount(mask) >= best) continue;
#            if (isSafeAfterShift(mask, n, h, u, pairs)) {
#                best = Integer.bitCount(mask);
#            }
#        }
#        return best;
#    }

#    private boolean isSafeAfterShift(int mask, int n, int h, int[] u, int[][] pairs) {
#        int[] shifted = new int[n];
#        for (int i = 0; i < n; i++) {
#            if (((mask >> i) & 1) == 1) shifted[i] = (u[i] + 1) % h;
#            else shifted[i] = u[i];
#        }
#        for (int[] p : pairs) {
#            int a = p[0] - 1, b = p[1] - 1;
#            if (shifted[a] == shifted[b]) return false;
#        }
#        return true;
#    }#
#
#    @Test void simpleCaseAnswerOne() {
#        int n = 5, h = 9;
#        int[] u = {0, 1, 3, 6, 8};
#        int[][] p = {{1, 2}, {2, 3}, {3, 4}, {4, 5}};
#        assertEquals(1, RelayWindowShift.minRelaysToShift(n, h, u, p));
#    }
#
#    @Test void connectedBidirectionalNeedsAll() {
#        int n = 4, h = 2;
#        int[] u = {0, 1, 0, 1};
#        int[][] p = {{1, 2}, {2, 3}, {3, 4}};
#        assertEquals(4, RelayWindowShift.minRelaysToShift(n, h, u, p));
#    }
#
#    @Test void wrapAroundInteraction() {
#        int n = 6, h = 5;
#        int[] u = {4, 0, 2, 3, 1, 4};
#        int[][] p = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}};
#        int expected = bruteMin(n, h, u, p);
#        assertEquals(expected, RelayWindowShift.minRelaysToShift(n, h, u, p));
#    }

#    @Test void multipleSmallCrossChecks() {
#        int[][] casesU = {
#            {0, 2, 4, 1, 3},
#            {1, 4, 0, 3, 2},
#            {2, 0, 3, 1, 4},
#            {3, 1, 4, 2, 0}
#        };
#        int[][][] casesP = {
#            {{1,2},{2,3},{3,4},{4,5}},
#            {{1,3},{2,4},{3,5},{1,5}},
#            {{1,2},{2,4},{4,5},{3,5}},
#            {{1,4},{2,5},{1,3},{3,4}}
#        };
#
#        int h = 5;
#        for (int i = 0; i < casesU.length; i++) {
#            int[] u = casesU[i];
#            int[][] p = casesP[i];
#            int expected = bruteMin(5, h, u, p);
#            int actual = RelayWindowShift.minRelaysToShift(5, h, u, p);
#            assertEquals(expected, actual);
#        }
#    }

#    @Test void exhaustiveOnTinyInstances() {
#        int n = 6, h = 4;
#        int[][] pairs = {{1,2},{2,3},{3,4},{4,5},{5,6},{1,6}};
#
#        int limit = 1;
#        for (int i = 0; i < n; i++) limit *= h;
#
#        for (int mask = 0; mask < limit; mask++) {
#            int x = mask;
#            int[] u = new int[n];
#            for (int i = 0; i < n; i++) {
#                u[i] = x % h;
#                x /= h;
#            }#
#
##           boolean valid = true;
#            for (int[] p : pairs) {
 #               if (u[p[0]-1] == u[p[1]-1]) { valid = false; break; }
#            }
#            if (!valid) continue;
#
#            int expected = bruteMin(n, h, u, pairs);
#            int actual = RelayWindowShift.minRelaysToShift(n, h, u, pairs);
#            assertEquals(expected, actual);
#        }
#    }##
#
#    @Test void performanceLargeShouldBeNearLinear() {
#        assertTimeoutPreemptively(Duration.ofSeconds(2), () -> {
#            int n = 100000;
#            int h = 200000;
#            int[] u = new int[n];
#            for (int i = 0; i < n; i++) u[i] = i;
#            int[][] p = new int[n - 1][2];
#            for (int i = 1; i < n; i++) {
#                p[i - 1][0] = i;
#                p[i - 1][1] = i + 1;
#            }
#            assertEquals(1, RelayWindowShift.minRelaysToShift(n, h, u, p));
#        });
#    }
#}
#""",
#    },

    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Tree Queries (Codeforces 1606F)
        # Source  : deepmind/code_contests  |  difficulty 12  |  201 tests
        # ──────────────────────────────────────────────────────────────────────
#──────────────────────────────────
"id": "corporate_consolidation_log112",
        "title": "Corporate Consolidation Strategy",
        "class_name": "CorporateConsolidation",

        "signature": "public static long[] calculateStrategy(int n, int[][] edges, int[][] queries)",

        "description": """\
A global corporation is organized as a hierarchy of `n` regional offices, indexed 1 to `n`. Office 1 serves as the global headquarters (the root). The connections between offices form a tree structure.

The board of directors is evaluating several independent restructuring plans. Each plan is defined by a target office `v` and a streamlining penalty `k`.

In a restructuring plan, you can choose to 'consolidate' any number of offices in the company's hierarchy, with two exceptions: you cannot consolidate the global headquarters (Office 1) or the target office `v`.

When an office is consolidated:
1. It is removed from the hierarchy.
2. All of its immediate subordinate offices are re-assigned to report directly to the consolidated office's former supervisor.

Your goal for each plan `(v, k)` is to maximize the 'Net Span of Control' for office `v`, calculated as:
Score = S - (M * k)

Where:
- S is the final number of immediate subordinates reporting directly to office `v` after all chosen consolidations are performed.
- M is the total number of offices consolidated across the entire company in that plan.
- k is the fixed overhead cost incurred for every office consolidated.

Note: Each plan is independent. Consolidations made for one query do not persist for the next.

Return an array of length `q` containing the maximum possible Score for each plan.

Constraints:
- 1 <= n <= 200,000
- 1 <= q <= 200,000
- 1 <= v <= n (v may be the headquarters)
- 0 <= k <= 200,000
- The input connections represent a valid tree structure.

""",


        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import java.time.Duration;

class CorporateConsolidationTest {

    @Test void DatasetCase001() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase002() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,1}, {7,200000}};
        long[] expected = {5, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase003() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {5, 2, 1, 5, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase004() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase005() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase006() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {5, 1, 1, 5, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase007() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase008() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 1, 4, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase009() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 0, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase010() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,0}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {5, 1, 5, 5, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase011() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase012() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase013() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,1}, {7,200000}};
        long[] expected = {5, 3, 2, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase014() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,3}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {5, 0, 1, 5, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase015() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase016() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {4, 1, 1, 4, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase017() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 0, 5, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase018() {
        int n = 8;
        int[][] edges = {{6,2}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {4, 1, 1, 4, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase019() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {4, 1, 0, 4, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase020() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {5, 1, 1, 4, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase021() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase022() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,0}, {7,0}, {5,1}, {5,200000}};
        long[] expected = {5, 1, 5, 5, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase023() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {7,69799}};
        long[] expected = {5, 2, 1, 4, 5, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase024() {
        int n = 8;
        int[][] edges = {{6,7}, {3,1}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase025() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,3}, {2,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {5, 0, 0, 5, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase026() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{2,0}, {1,2}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {0, 1, 1, 4, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase027() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 5, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase028() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,3}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase029() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}};
        long[] expected = {5};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase030() {
        int n = 8;
        int[][] edges = {{6,2}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {2, 1, 1, 4, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase031() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 1, 1, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase032() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {2, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase033() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {6,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase034() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {5, 2, 0, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase035() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,2}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 0, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase036() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {3,1}, {8,1}, {7,69799}};
        long[] expected = {5, 2, 1, 2, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase037() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {1,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 2, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase038() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,2}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {3, 1, 1, 3, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase039() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 2, 0, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase040() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {3,1}, {7,200000}};
        long[] expected = {5, 3, 2, 4, 1, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase041() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,6}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 3, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase042() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}};
        long[] expected = {3, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase043() {
        int n = 8;
        int[][] edges = {{6,7}, {3,1}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {5,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 1, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase044() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {0, 1, 0, 4, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase045() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,1}, {2,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 0, 1, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase046() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {5,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 1, 3, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase047() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {6,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 2, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase048() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,1}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {3,1}, {8,1}, {7,69799}};
        long[] expected = {5, 2, 2, 2, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase049() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,2}, {5,0}, {7,200000}};
        long[] expected = {4, 0, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase050() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {4,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {3,1}, {7,200000}};
        long[] expected = {4, 2, 2, 3, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase051() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {7,120567}};
        long[] expected = {4, 2, 1, 4, 4, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase052() {
        int n = 8;
        int[][] edges = {{6,3}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {0, 1, 0, 4, 2, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase053() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {2,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 2, 1, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase054() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,5}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,1}, {2,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 0, 1, 2, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase055() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,6}, {3,4}, {7,1}, {5,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 1, 2, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase056() {
        int n = 8;
        int[][] edges = {{6,1}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,2}, {5,0}, {7,200000}};
        long[] expected = {5, 0, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase057() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}};
        long[] expected = {4, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase058() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {2,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {2, 2, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase059() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,2}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 2, 2, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase060() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {3,0}, {5,1}, {7,200000}};
        long[] expected = {4, 2, 1, 1, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase061() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 0, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase062() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {5, 2, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase063() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 3, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase064() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {4, 1, 0, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase065() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {8,1}, {4,200000}};
        long[] expected = {5, 3, 2, 4, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase066() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {4,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {4, 1, 1, 2, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase067() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase068() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,2}};
        int[][] queries = {{2,0}, {1,3}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 1, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase069() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,2}};
        int[][] queries = {{2,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase070() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,5}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,0}, {5,1}, {7,7365}};
        long[] expected = {4, 1, 1, 4, 2, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase071() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {5,2}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 1, 3, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase072() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,6}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,2}, {5,0}, {7,200000}};
        long[] expected = {3, 0, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase073() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {2,2}, {1,3}};
        long[] expected = {3, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase074() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,5}, {5,7}, {7,4}, {8,1}, {1,3}};
        int[][] queries = {{1,1}, {2,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {2, 0, 2, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase075() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {2,6}, {3,4}, {7,1}, {5,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 2, 3, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase076() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {3,0}, {5,1}, {4,200000}};
        long[] expected = {4, 2, 1, 1, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase077() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {4, 1, 0, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase078() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}};
        long[] expected = {4, 2, 1, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase079() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,3}, {7,1}, {8,1}, {4,200000}};
        long[] expected = {0, 3, 2, 4, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase080() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {3, 2, 0, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase081() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {6,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {8,1}, {3,1}, {7,200000}};
        long[] expected = {4, 2, 2, 0, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase082() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {3,2}, {1,3}};
        long[] expected = {3, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase083() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {4,1}, {8,2}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {3,1}, {7,68507}};
        long[] expected = {3, 2, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase084() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,1}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,3}, {7,1}, {8,1}, {4,200000}};
        long[] expected = {0, 3, 3, 3, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase085() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,4}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {2, 2, 0, 0, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase086() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {6,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,2}, {7,200000}};
        long[] expected = {3, 1, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase087() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,4}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {2, 2, 2, 0, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase088() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase089() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,3}, {7,0}, {7,1}, {7,200000}};
        long[] expected = {5, 1, 1, 5, 4, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase090() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {7,0}, {5,1}};
        long[] expected = {1, 2, 1, 4, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase091() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,1}, {3,200000}};
        long[] expected = {4, 1, 1, 3, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase092() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,8}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 3, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase093() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {4, 1, 1, 3, 1, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase094() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,1}, {1,0}, {7,69799}};
        long[] expected = {5, 3, 1, 4, 5, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase095() {
        int n = 8;
        int[][] edges = {{6,7}, {3,1}, {8,1}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {0, 3, 0, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase096() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,2}};
        int[][] queries = {{1,1}, {1,2}, {2,0}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {2, 1, 2, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase097() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,2}, {1,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {1,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase098() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,2}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {3, 3, 1, 3, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase099() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {4,120567}};
        long[] expected = {5, 2, 1, 4, 5, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase100() {
        int n = 8;
        int[][] edges = {{6,7}, {3,1}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {5,0}, {3,1}, {7,200000}};
        long[] expected = {1, 2, 1, 0, 2, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase101() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,8}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 1, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase102() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {6,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {1,1}, {7,200000}};
        long[] expected = {4, 2, 2, 3, 3, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase103() {
        int n = 8;
        int[][] edges = {{6,1}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}};
        long[] expected = {5, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase104() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {2,5}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {2, 2, 2, 2, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase105() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {6,2}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {3,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {2, 0, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase106() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,4}, {1,2}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 2, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase107() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,2}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {3,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 1, 2, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase108() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {5, 5, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase109() {
        int n = 8;
        int[][] edges = {{6,3}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,3}, {7,0}, {5,1}, {7,121089}};
        long[] expected = {5, 1, 1, 5, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase110() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {7,1}, {5,0}, {7,106177}};
        long[] expected = {2, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase111() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,2}};
        int[][] queries = {{2,1}, {1,0}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 4, 1, 4, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase112() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {5,4}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 3, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase113() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,5}, {5,7}, {7,4}, {8,1}, {1,3}};
        int[][] queries = {{2,1}, {2,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {0, 0, 2, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase114() {
        int n = 8;
        int[][] edges = {{6,7}, {1,2}, {8,5}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,7365}};
        long[] expected = {5, 2, 2, 4, 2, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase115() {
        int n = 8;
        int[][] edges = {{6,7}, {1,2}, {8,1}, {5,7}, {7,4}, {6,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {8,1}, {3,1}, {7,200000}};
        long[] expected = {5, 3, 3, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase116() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,4}, {7,1}, {7,1}, {7,200000}};
        long[] expected = {4, 1, 1, 3, 3, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase117() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,2}, {5,7}, {7,4}, {2,1}, {6,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,2}, {7,200000}};
        long[] expected = {3, 1, 2, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase118() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,2}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {5, 3, 3, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase119() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,3}, {7,0}, {7,1}, {7,200000}};
        long[] expected = {4, 1, 1, 4, 4, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase120() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {1,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {8,0}, {7,69799}};
        long[] expected = {4, 2, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase121() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {3,200000}};
        long[] expected = {4, 1, 1, 3, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase122() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {4,1}, {7,3}};
        int[][] queries = {{2,0}, {1,1}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase123() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {4, 4, 1, 3, 1, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase124() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,4}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,1}, {1,0}, {7,69799}};
        long[] expected = {4, 3, 1, 4, 4, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase125() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {4,2}, {1,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {1,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 1, 3, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase126() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {3,1}, {3,73575}};
        long[] expected = {5, 3, 2, 4, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase127() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {4,120567}};
        long[] expected = {5, 2, 2, 3, 5, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase128() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,8}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{4,0}, {1,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {0, 1, 1, 1, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase129() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,3}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {2,5}, {1,3}, {7,0}, {7,1}, {7,200000}};
        long[] expected = {3, 1, 1, 2, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase130() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,1}, {3,4}, {7,1}, {5,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {2, 2, 1, 2, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase131() {
        int n = 8;
        int[][] edges = {{6,1}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {2,2}};
        long[] expected = {0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase132() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {2,1}, {7,2}};
        int[][] queries = {{2,1}, {1,0}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {2, 4, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase133() {
        int n = 8;
        int[][] edges = {{6,5}, {3,2}, {8,5}, {5,7}, {7,4}, {8,1}, {1,3}};
        int[][] queries = {{2,1}, {2,2}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {0, 0, 2, 1, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase134() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {4,1}, {7,2}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,1}, {3,1}, {2,68507}};
        long[] expected = {4, 2, 2, 3, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase135() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,1}, {2,2}, {1,3}};
        long[] expected = {1, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase136() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {3,1}, {5,3}};
        int[][] queries = {{1,0}, {3,2}, {1,3}};
        long[] expected = {4, 3, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase137() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,1}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {5, 3, 4, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase138() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {1,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {4, 4, 2, 3, 1, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase139() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,4}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {4,1}, {1,0}, {7,69799}};
        long[] expected = {4, 3, 1, 1, 4, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase140() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,2}, {1,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {4,120567}};
        long[] expected = {4, 1, 1, 3, 4, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase141() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,8}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{4,0}, {1,5}, {1,3}, {7,0}, {5,1}, {4,200000}};
        long[] expected = {0, 1, 1, 1, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase142() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {2,5}, {1,3}, {7,0}, {7,1}, {7,200000}};
        long[] expected = {3, 2, 1, 2, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase143() {
        int n = 8;
        int[][] edges = {{6,8}, {3,4}, {8,2}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {2,4}, {1,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {1, 1, 2, 2, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase144() {
        int n = 8;
        int[][] edges = {{6,7}, {1,2}, {8,1}, {5,2}, {7,4}, {6,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {8,1}, {3,1}, {7,119289}};
        long[] expected = {4, 3, 3, 0, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase145() {
        int n = 8;
        int[][] edges = {{6,7}, {6,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {3,2}, {1,3}};
        long[] expected = {2, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase146() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,1}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {4, 3, 4, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase147() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,6}, {7,4}, {7,1}, {7,2}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,1}, {8,1}, {5,69799}};
        long[] expected = {3, 1, 1, 3, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase148() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {1,4}, {8,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,1}, {8,0}, {7,69799}};
        long[] expected = {3, 2, 2, 1, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase149() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,4}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {4,1}, {1,0}, {7,69799}};
        long[] expected = {5, 3, 1, 2, 5, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase150() {
        int n = 8;
        int[][] edges = {{6,5}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,7}, {2,0}, {5,2}, {6,200000}};
        long[] expected = {3, 1, 1, 3, 1, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase151() {
        int n = 8;
        int[][] edges = {{6,7}, {6,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {3,0}, {1,3}};
        long[] expected = {2, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase152() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {8,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,1}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {3, 2, 3, 3, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase153() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {2,4}, {8,1}, {7,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,1}, {8,0}, {7,69799}};
        long[] expected = {2, 1, 1, 1, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase154() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,4}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {4,1}, {1,0}, {7,69799}};
        long[] expected = {5, 5, 1, 2, 5, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase155() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,2}, {1,4}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {1,0}, {4,120567}};
        long[] expected = {3, 1, 1, 3, 3, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase156() {
        int n = 8;
        int[][] edges = {{6,5}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,1}, {1,2}, {1,7}, {2,0}, {5,2}, {6,200000}};
        long[] expected = {2, 1, 1, 3, 1, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase157() {
        int n = 8;
        int[][] edges = {{6,7}, {6,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {4,0}, {1,3}};
        long[] expected = {2, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase158() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {8,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,0}, {7,1}, {8,1}, {7,200000}};
        long[] expected = {3, 2, 4, 3, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase159() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,4}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,0}, {1,2}, {4,1}, {1,0}, {7,69799}};
        long[] expected = {5, 5, 2, 2, 5, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase160() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,2}, {1,4}};
        int[][] queries = {{1,0}};
        long[] expected = {3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase161() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {8,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,0}, {8,1}, {8,1}, {7,200000}};
        long[] expected = {3, 2, 4, 1, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase162() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,4}, {5,7}, {7,4}, {8,1}, {7,3}};
        int[][] queries = {{1,0}, {1,0}, {1,2}, {4,1}, {1,0}, {7,69799}};
        long[] expected = {4, 4, 1, 3, 4, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase163() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {7,1}, {5,1}, {7,200000}};
        long[] expected = {3, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase164() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,1}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 2, 1, 4, 1, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase165() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,3}, {7,1}, {8,1}, {7,69799}};
        long[] expected = {0, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase166() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,0}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {4, 1, 4, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase167() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{4,0}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {0, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase168() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {1,3}};
        int[][] queries = {{2,0}, {1,2}, {1,6}, {8,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 2, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase169() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {8,0}, {5,0}, {7,200000}};
        long[] expected = {5, 1, 0, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase170() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {4, 1, 1, 3, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase171() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,1}, {1,2}, {1,3}, {4,0}, {5,1}, {7,200000}};
        long[] expected = {1, 1, 1, 0, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase172() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,6}, {5,7}, {3,4}, {6,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {3, 1, 0, 1, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase173() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,1}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {3,200000}};
        long[] expected = {0, 2, 0, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase174() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {5,1}, {5,2}};
        int[][] queries = {{1,1}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 1, 1, 3, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase175() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {1,0}, {5,120567}};
        long[] expected = {4, 2, 1, 4, 4, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase176() {
        int n = 8;
        int[][] edges = {{6,3}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,1}, {2,200000}};
        long[] expected = {0, 1, 0, 4, 2, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase177() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {6,3}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,1}, {1,1}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {1, 2, 2, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase178() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}, {1,2}, {7,1}, {5,0}, {7,200000}};
        long[] expected = {5, 0, 2, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase179() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 1, 0, 3, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase180() {
        int n = 8;
        int[][] edges = {{6,5}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,1}, {1,2}, {1,6}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {2, 1, 1, 2, 1, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase181() {
        int n = 8;
        int[][] edges = {{6,7}, {6,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,1}, {3,1}, {7,200000}};
        long[] expected = {5, 3, 0, 4, 0, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase182() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {3,0}, {5,1}, {4,200000}};
        long[] expected = {5, 3, 2, 1, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase183() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {3,4}, {3,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,3}, {7,0}, {5,0}, {7,200000}};
        long[] expected = {4, 1, 0, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase184() {
        int n = 8;
        int[][] edges = {{6,7}, {4,2}, {8,3}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {1,3}, {7,1}};
        long[] expected = {0, 2, 1, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase185() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {7,0}, {5,2}, {7,200000}};
        long[] expected = {2, 2, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase186() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {3,0}};
        long[] expected = {4, 2, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase187() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,2}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,6}, {7,0}, {5,1}};
        long[] expected = {4, 2, 1, 4, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase188() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {7,4}, {7,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {5,1}, {3,200000}};
        long[] expected = {4, 1, 1, 3, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase189() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,1}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {3, 2, 2, 3, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase190() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {2,2}, {1,3}, {7,1}, {3,1}, {7,73575}};
        long[] expected = {5, 0, 2, 4, 1, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase191() {
        int n = 8;
        int[][] edges = {{6,7}, {1,2}, {8,3}, {5,7}, {7,4}, {8,1}, {5,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}};
        long[] expected = {3, 2, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase192() {
        int n = 8;
        int[][] edges = {{6,7}, {3,1}, {8,2}, {5,7}, {7,4}, {2,1}, {7,3}};
        int[][] queries = {{2,0}, {1,2}, {2,3}, {5,0}, {3,1}, {2,200000}};
        long[] expected = {1, 2, 1, 0, 2, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase193() {
        int n = 8;
        int[][] edges = {{6,8}, {3,2}, {6,2}, {5,7}, {8,4}, {2,1}, {7,1}};
        int[][] queries = {{2,0}, {3,5}, {1,3}, {7,0}, {5,1}, {7,200000}};
        long[] expected = {2, 0, 2, 1, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase194() {
        int n = 8;
        int[][] edges = {{6,3}, {3,2}, {8,3}, {5,7}, {7,4}, {3,1}, {7,3}};
        int[][] queries = {{1,0}, {1,3}, {1,3}, {7,0}, {5,1}, {7,121089}};
        long[] expected = {5, 1, 1, 2, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase195() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {8,1}, {7,3}};
        int[][] queries = {{1,1}, {1,4}, {2,3}, {2,0}, {5,0}, {7,200000}};
        long[] expected = {1, 1, 0, 0, 0, 2};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase196() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,3}, {5,7}, {3,4}, {7,1}, {7,2}};
        int[][] queries = {{2,1}, {1,0}, {2,3}, {7,0}, {5,0}, {2,200000}};
        long[] expected = {1, 4, 1, 4, 0, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase197() {
        int n = 8;
        int[][] edges = {{6,7}, {1,2}, {8,1}, {5,7}, {7,4}, {6,2}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {8,1}, {3,1}, {7,200000}};
        long[] expected = {4, 2, 2, 0, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase198() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,5}, {5,7}, {7,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {2,4}, {7,1}, {5,0}, {7,129480}};
        long[] expected = {4, 2, 0, 4, 1, 4};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase199() {
        int n = 8;
        int[][] edges = {{6,7}, {3,2}, {8,1}, {5,7}, {3,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {4,3}, {3,1}, {5,0}, {7,200000}};
        long[] expected = {5, 2, 0, 2, 0, 3};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase200() {
        int n = 8;
        int[][] edges = {{6,4}, {3,2}, {8,3}, {5,7}, {1,4}, {7,1}, {7,3}};
        int[][] queries = {{1,0}, {1,2}, {1,3}, {7,1}, {8,0}, {6,69799}};
        long[] expected = {4, 2, 2, 2, 0, 0};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    @Test void DatasetCase201() {
        int n = 8;
        int[][] edges = {{6,7}, {5,2}, {8,3}, {5,7}, {3,4}, {7,1}, {6,3}};
        int[][] queries = {{1,0}, {1,0}, {1,3}, {7,1}, {5,0}, {6,200000}};
        long[] expected = {3, 3, 1, 2, 1, 1};
        assertArrayEquals(expected, CorporateConsolidation.calculateStrategy(n, edges, queries));
    }

    


}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Deque End-Pick Game
        #        Original: Codeforces 1600E - Array Game

        # ──────────────────────────────────────────────────────────────────────
        "id": "expedition_ascent_log112",
        "title": "The Ridge Ascent Duel",
        "class_name": "DuelExpeditionAscent",

        "signature": "public static String solve(String input)",

        "description": """\
Two climbers, A and B, are standing at the opposite ends of a narrow ridge represented by a sequence of N peak elevations. They are collaborating to build a single shared climbing log, but competing to be the one who makes the final entry.

Climber A goes first. On each turn, the current climber must choose one peak from either the leftmost or the rightmost end of the remaining ridge. Once a peak is chosen, it is removed from the ridge and its elevation is recorded in the shared log.

Crucially, the shared log must be strictly ascending. This means every new elevation added must be strictly greater than the one previously recorded. If a climber cannot pick a peak from either available end that is higher than the last entry in the log, they are stuck and lose the duel. The last climber to successfully make a move wins.

Both climbers use a perfect strategy to ensure their own victory. Determine the winner.

Input format:
  Line 1: N (the number of peaks)
  Line 2: N space-separated integers (elevations of each peak)

Output format:
  A single string: "Alice" (for Climber A) or "Bob" (for Climber B).

The solution must include full parsing of the input string and return the formatted result in `solve(String input)`.""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class DuelExpeditionAscentTest {

    private static String norm(String s) {
        if (s == null) return "";
        s = s.replace("\\r\\n", "\\n").replace("\\r", "\\n");
        String[] lines = s.split("\\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            int end = line.length();
            while (end > 0 && Character.isWhitespace(line.charAt(end - 1))) end--;
            sb.append(line, 0, end).append('\\n');
        }
        return sb.toString().trim();
    }

    private void assertCase(String input, String expected) {
        String actual = DuelExpeditionAscent.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    @Test void case001() { assertCase("6\\n5 8 2 1 10 9\\n", "Bob\\n"); }
    @Test void case002() { assertCase("3\\n5 4 5\\n", "Alice\\n"); }
    @Test void case003() { assertCase("1\\n5\\n", "Alice\\n"); }
    @Test void case004() { assertCase("3\\n5 6 5\\n", "Bob\\n"); }
    @Test void case005() { assertCase("2\\n5 12\\n", "Alice\\n"); }
    @Test void case006() { assertCase("3\\n5 6 9\\n", "Alice\\n"); }
    @Test void case007() { assertCase("6\\n2 6 0 0 5 0\\n", "Bob\\n"); }
    @Test void case008() { assertCase("2\\n5 2\\n", "Alice\\n"); }
    @Test void case009() { assertCase("6\\n5 4 2 1 10 9\\n", "Alice\\n"); }
    @Test void case010() { assertCase("3\\n5 1 5\\n", "Alice\\n"); }
    @Test void case011() { assertCase("1\\n2\\n", "Alice\\n"); }
    @Test void case012() { assertCase("3\\n5 6 10\\n", "Alice\\n"); }
    @Test void case013() { assertCase("2\\n5 3\\n", "Alice\\n"); }
    @Test void case014() { assertCase("6\\n4 4 2 1 10 9\\n", "Alice\\n"); }
    @Test void case015() { assertCase("3\\n7 1 5\\n", "Alice\\n"); }
    @Test void case016() { assertCase("1\\n3\\n", "Alice\\n"); }
    @Test void case017() { assertCase("2\\n5 5\\n", "Alice\\n"); }
    @Test void case018() { assertCase("6\\n4 3 2 1 10 9\\n", "Alice\\n"); }
    @Test void case019() { assertCase("3\\n7 1 3\\n", "Alice\\n"); }
    @Test void case020() { assertCase("1\\n1\\n", "Alice\\n"); }
    @Test void case021() { assertCase("2\\n5 7\\n", "Alice\\n"); }
    @Test void case022() { assertCase("6\\n4 3 2 0 10 9\\n", "Alice\\n"); }
    @Test void case023() { assertCase("3\\n7 1 1\\n", "Alice\\n"); }
    @Test void case024() { assertCase("1\\n0\\n", "Alice\\n"); }
    @Test void case025() { assertCase("2\\n5 0\\n", "Alice\\n"); }
    @Test void case026() { assertCase("6\\n4 3 2 0 12 9\\n", "Alice\\n"); }
    @Test void case027() { assertCase("3\\n7 1 2\\n", "Alice\\n"); }
    @Test void case028() { assertCase("1\\n4\\n", "Alice\\n"); }
    @Test void case029() { assertCase("2\\n10 0\\n", "Alice\\n"); }
    @Test void case030() { assertCase("6\\n4 3 0 0 12 9\\n", "Alice\\n"); }
    @Test void case031() { assertCase("3\\n13 1 2\\n", "Alice\\n"); }
    @Test void case032() { assertCase("2\\n0 0\\n", "Alice\\n"); }
    @Test void case033() { assertCase("6\\n4 3 0 0 12 6\\n", "Alice\\n"); }
    @Test void case034() { assertCase("3\\n13 1 4\\n", "Alice\\n"); }
    @Test void case035() { assertCase("2\\n1 0\\n", "Alice\\n"); }
    @Test void case036() { assertCase("6\\n4 3 0 0 14 6\\n", "Alice\\n"); }
    @Test void case037() { assertCase("3\\n13 2 4\\n", "Alice\\n"); }
    @Test void case038() { assertCase("2\\n1 1\\n", "Alice\\n"); }
    @Test void case039() { assertCase("6\\n7 3 0 0 14 6\\n", "Alice\\n"); }
    @Test void case040() { assertCase("3\\n13 0 4\\n", "Alice\\n"); }
    @Test void case041() { assertCase("2\\n0 1\\n", "Alice\\n"); }
    @Test void case042() { assertCase("6\\n7 3 0 0 14 5\\n", "Alice\\n"); }
    @Test void case043() { assertCase("3\\n4 0 4\\n", "Alice\\n"); }
    @Test void case044() { assertCase("2\\n0 2\\n", "Alice\\n"); }
    @Test void case045() { assertCase("6\\n7 4 0 0 14 5\\n", "Alice\\n"); }
    @Test void case046() { assertCase("3\\n4 0 0\\n", "Alice\\n"); }
    @Test void case047() { assertCase("2\\n0 4\\n", "Alice\\n"); }
    @Test void case048() { assertCase("6\\n7 4 0 0 17 5\\n", "Alice\\n"); }
    @Test void case049() { assertCase("3\\n6 0 0\\n", "Alice\\n"); }
    @Test void case050() { assertCase("2\\n1 4\\n", "Alice\\n"); }
    @Test void case051() { assertCase("6\\n7 4 0 0 17 6\\n", "Alice\\n"); }
    @Test void case052() { assertCase("3\\n6 1 0\\n", "Alice\\n"); }
    @Test void case053() { assertCase("2\\n2 4\\n", "Alice\\n"); }
    @Test void case054() { assertCase("6\\n7 4 0 0 17 11\\n", "Alice\\n"); }
    @Test void case055() { assertCase("3\\n6 1 -1\\n", "Alice\\n"); }
    @Test void case056() { assertCase("2\\n1 8\\n", "Alice\\n"); }
    @Test void case057() { assertCase("6\\n7 6 0 0 17 11\\n", "Alice\\n"); }
    @Test void case058() { assertCase("3\\n6 1 -2\\n", "Alice\\n"); }
    @Test void case059() { assertCase("2\\n1 -1\\n", "Alice\\n"); }
    @Test void case060() { assertCase("6\\n7 6 0 0 17 12\\n", "Alice\\n"); }
    @Test void case061() { assertCase("3\\n6 0 -2\\n", "Alice\\n"); }
    @Test void case062() { assertCase("2\\n0 -1\\n", "Alice\\n"); }
    @Test void case063() { assertCase("6\\n6 6 0 0 17 12\\n", "Alice\\n"); }
    @Test void case064() { assertCase("3\\n9 0 0\\n", "Alice\\n"); }
    @Test void case065() { assertCase("2\\n0 -2\\n", "Alice\\n"); }
    @Test void case066() { assertCase("6\\n6 6 0 0 5 12\\n", "Alice\\n"); }
    @Test void case067() { assertCase("3\\n15 0 0\\n", "Alice\\n"); }
    @Test void case068() { assertCase("6\\n2 6 0 0 5 12\\n", "Alice\\n"); }
    @Test void case069() { assertCase("3\\n15 1 0\\n", "Alice\\n"); }
    @Test void case070() { assertCase("3\\n15 0 1\\n", "Alice\\n"); }
    @Test void case071() { assertCase("6\\n2 9 0 0 5 0\\n", "Bob\\n"); }
    @Test void case072() { assertCase("6\\n2 12 0 0 5 0\\n", "Bob\\n"); }
    @Test void case073() { assertCase("6\\n2 7 0 0 5 0\\n", "Bob\\n"); }
    @Test void case074() { assertCase("6\\n2 7 0 0 2 0\\n", "Bob\\n"); }
    @Test void case075() { assertCase("6\\n2 7 1 0 2 0\\n", "Bob\\n"); }
    @Test void case076() { assertCase("6\\n1 7 1 0 2 0\\n", "Bob\\n"); }
    @Test void case077() { assertCase("6\\n1 0 1 0 2 0\\n", "Alice\\n"); }
    @Test void case078() { assertCase("6\\n1 0 2 0 2 0\\n", "Alice\\n"); }
    @Test void case079() { assertCase("6\\n0 0 2 0 2 0\\n", "Alice\\n"); }
    @Test void case080() { assertCase("3\\n5 7 10\\n", "Alice\\n"); }
    @Test void case081() { assertCase("2\\n4 12\\n", "Alice\\n"); }
    @Test void case082() { assertCase("6\\n5 8 0 1 10 9\\n", "Bob\\n"); }
    @Test void case083() { assertCase("3\\n5 8 5\\n", "Bob\\n"); }
    @Test void case084() { assertCase("1\\n8\\n", "Alice\\n"); }
    @Test void case085() { assertCase("3\\n5 6 11\\n", "Alice\\n"); }
    @Test void case086() { assertCase("2\\n3 2\\n", "Alice\\n"); }
    @Test void case087() { assertCase("6\\n5 4 4 1 10 9\\n", "Alice\\n"); }
    @Test void case088() { assertCase("3\\n2 1 5\\n", "Alice\\n"); }
    @Test void case089() { assertCase("3\\n5 8 10\\n", "Alice\\n"); }
    @Test void case090() { assertCase("2\\n9 3\\n", "Alice\\n"); }
    @Test void case091() { assertCase("6\\n4 8 2 1 10 9\\n", "Bob\\n"); }
    @Test void case092() { assertCase("3\\n7 2 5\\n", "Alice\\n"); }
    @Test void case093() { assertCase("2\\n-1 2\\n", "Alice\\n"); }
    @Test void case094() { assertCase("6\\n4 3 2 1 0 9\\n", "Alice\\n"); }
    @Test void case095() { assertCase("3\\n6 1 3\\n", "Alice\\n"); }
    @Test void case096() { assertCase("2\\n9 7\\n", "Alice\\n"); }
    @Test void case097() { assertCase("6\\n4 0 2 0 10 9\\n", "Alice\\n"); }
    @Test void case098() { assertCase("3\\n7 1 0\\n", "Alice\\n"); }
    @Test void case099() { assertCase("2\\n5 1\\n", "Alice\\n"); }
    @Test void case100() { assertCase("6\\n4 3 2 0 12 11\\n", "Alice\\n"); }
    @Test void case101() { assertCase("3\\n7 0 2\\n", "Alice\\n"); }
    @Test void case102() { assertCase("1\\n6\\n", "Alice\\n"); }
    @Test void case103() { assertCase("2\\n16 0\\n", "Alice\\n"); }
    @Test void case104() { assertCase("6\\n4 3 0 -1 12 9\\n", "Alice\\n"); }
    @Test void case105() { assertCase("3\\n17 1 2\\n", "Alice\\n"); }
    @Test void case106() { assertCase("2\\n-1 0\\n", "Alice\\n"); }
    @Test void case107() { assertCase("6\\n6 3 0 0 12 6\\n", "Alice\\n"); }
    @Test void case108() { assertCase("3\\n21 1 4\\n", "Alice\\n"); }
    @Test void case109() { assertCase("2\\n2 -1\\n", "Alice\\n"); }
    @Test void case110() { assertCase("6\\n1 3 0 0 14 6\\n", "Bob\\n"); }
    @Test void case111() { assertCase("3\\n23 2 4\\n", "Alice\\n"); }
    @Test void case112() { assertCase("2\\n1 2\\n", "Alice\\n"); }
    @Test void case113() { assertCase("6\\n7 3 0 -1 14 6\\n", "Alice\\n"); }
    @Test void case114() { assertCase("3\\n17 0 4\\n", "Alice\\n"); }
    @Test void case115() { assertCase("2\\n0 3\\n", "Alice\\n"); }
    @Test void case116() { assertCase("6\\n7 3 0 0 28 5\\n", "Alice\\n"); }
    @Test void case117() { assertCase("3\\n4 0 5\\n", "Alice\\n"); }
    @Test void case118() { assertCase("2\\n1 3\\n", "Alice\\n"); }
    @Test void case119() { assertCase("6\\n7 4 0 1 14 5\\n", "Alice\\n"); }
    @Test void case120() { assertCase("3\\n7 0 0\\n", "Alice\\n"); }
    @Test void case121() { assertCase("2\\n1 -2\\n", "Alice\\n"); }
    @Test void case122() { assertCase("6\\n7 4 -1 0 17 5\\n", "Alice\\n"); }
    @Test void case123() { assertCase("3\\n6 1 1\\n", "Alice\\n"); }
    @Test void case124() { assertCase("2\\n1 7\\n", "Alice\\n"); }
    @Test void case125() { assertCase("6\\n7 4 0 1 17 6\\n", "Alice\\n"); }
    @Test void case126() { assertCase("3\\n8 1 0\\n", "Alice\\n"); }
    @Test void case127() { assertCase("2\\n2 2\\n", "Alice\\n"); }
    @Test void case128() { assertCase("6\\n7 4 0 0 17 7\\n", "Alice\\n"); }
    @Test void case129() { assertCase("3\\n11 0 0\\n", "Alice\\n"); }
    @Test void case130() { assertCase("2\\n2 8\\n", "Alice\\n"); }
    @Test void case131() { assertCase("6\\n4 6 0 0 17 11\\n", "Bob\\n"); }
    @Test void case132() { assertCase("3\\n7 0 -2\\n", "Alice\\n"); }
    @Test void case133() { assertCase("2\\n2 -2\\n", "Alice\\n"); }
    @Test void case134() { assertCase("6\\n7 6 0 0 17 5\\n", "Alice\\n"); }
    @Test void case135() { assertCase("3\\n11 0 -2\\n", "Alice\\n"); }
    @Test void case136() { assertCase("2\\n-1 1\\n", "Alice\\n"); }
    @Test void case137() { assertCase("6\\n0 6 0 0 17 12\\n", "Bob\\n"); }
    @Test void case138() { assertCase("3\\n9 1 0\\n", "Alice\\n"); }
    @Test void case139() { assertCase("6\\n6 6 0 0 5 10\\n", "Alice\\n"); }
    @Test void case140() { assertCase("3\\n5 0 0\\n", "Alice\\n"); }
    @Test void case141() { assertCase("6\\n2 7 0 0 5 12\\n", "Alice\\n"); }
    @Test void case142() { assertCase("3\\n15 2 0\\n", "Alice\\n"); }
    @Test void case143() { assertCase("6\\n2 6 0 0 4 0\\n", "Bob\\n"); }
    @Test void case144() { assertCase("3\\n15 1 1\\n", "Alice\\n"); }
    @Test void case145() { assertCase("6\\n3 9 0 0 5 0\\n", "Bob\\n"); }
    @Test void case146() { assertCase("6\\n1 12 0 0 5 0\\n", "Bob\\n"); }
    @Test void case147() { assertCase("6\\n2 7 0 0 7 0\\n", "Bob\\n"); }
    @Test void case148() { assertCase("6\\n2 7 0 0 3 0\\n", "Bob\\n"); }
    @Test void case149() { assertCase("6\\n2 0 1 0 2 0\\n", "Alice\\n"); }
    @Test void case150() { assertCase("6\\n1 6 1 0 2 0\\n", "Bob\\n"); }
    @Test void case151() { assertCase("6\\n1 0 3 0 2 0\\n", "Alice\\n"); }
    @Test void case152() { assertCase("3\\n10 7 10\\n", "Alice\\n"); }
    @Test void case153() { assertCase("2\\n1 12\\n", "Alice\\n"); }
    @Test void case154() { assertCase("6\\n8 8 0 1 10 9\\n", "Alice\\n"); }
    @Test void case155() { assertCase("1\\n10\\n", "Alice\\n"); }
    @Test void case156() { assertCase("3\\n8 6 11\\n", "Alice\\n"); }
    @Test void case157() { assertCase("2\\n3 4\\n", "Alice\\n"); }
    @Test void case158() { assertCase("6\\n5 4 4 2 10 9\\n", "Alice\\n"); }
    @Test void case159() { assertCase("3\\n2 2 5\\n", "Alice\\n"); }
    @Test void case160() { assertCase("3\\n5 9 10\\n", "Alice\\n"); }
    @Test void case161() { assertCase("2\\n14 3\\n", "Alice\\n"); }
    @Test void case162() { assertCase("6\\n4 8 4 1 10 9\\n", "Bob\\n"); }
    @Test void case163() { assertCase("3\\n10 2 5\\n", "Alice\\n"); }
    @Test void case164() { assertCase("2\\n-1 3\\n", "Alice\\n"); }
    @Test void case165() { assertCase("6\\n4 3 2 1 0 13\\n", "Alice\\n"); }
    @Test void case166() { assertCase("3\\n6 0 3\\n", "Alice\\n"); }
    @Test void case167() { assertCase("2\\n15 7\\n", "Alice\\n"); }
    @Test void case168() { assertCase("6\\n4 1 2 0 10 9\\n", "Alice\\n"); }
    @Test void case169() { assertCase("3\\n7 2 0\\n", "Alice\\n"); }
    @Test void case170() { assertCase("2\\n2 0\\n", "Alice\\n"); }
    @Test void case171() { assertCase("6\\n4 3 2 0 8 11\\n", "Alice\\n"); }
    @Test void case172() { assertCase("3\\n3 0 2\\n", "Alice\\n"); }
    @Test void case173() { assertCase("1\\n9\\n", "Alice\\n"); }
    @Test void case174() { assertCase("2\\n4 0\\n", "Alice\\n"); }
    @Test void case175() { assertCase("6\\n4 3 0 -1 6 9\\n", "Alice\\n"); }
    @Test void case176() { assertCase("3\\n17 2 2\\n", "Alice\\n"); }
    @Test void case177() { assertCase("2\\n-2 0\\n", "Alice\\n"); }
    @Test void case178() { assertCase("6\\n5 3 0 0 12 6\\n", "Alice\\n"); }
    @Test void case179() { assertCase("3\\n21 1 5\\n", "Alice\\n"); }
    @Test void case180() { assertCase("2\\n2 1\\n", "Alice\\n"); }
    @Test void case181() { assertCase("6\\n1 3 1 0 14 6\\n", "Bob\\n"); }
    @Test void case182() { assertCase("3\\n23 3 4\\n", "Alice\\n"); }
    @Test void case183() { assertCase("2\\n-1 4\\n", "Alice\\n"); }
    @Test void case184() { assertCase("6\\n7 3 0 -1 14 0\\n", "Alice\\n"); }
    @Test void case185() { assertCase("2\\n0 8\\n", "Alice\\n"); }
    @Test void case186() { assertCase("6\\n7 3 0 -1 28 5\\n", "Alice\\n"); }
    @Test void case187() { assertCase("3\\n4 0 1\\n", "Alice\\n"); }
    @Test void case188() { assertCase("2\\n1 5\\n", "Alice\\n"); }
    @Test void case189() { assertCase("6\\n7 4 1 1 14 5\\n", "Alice\\n"); }
    @Test void case190() { assertCase("3\\n12 0 0\\n", "Alice\\n"); }
    @Test void case191() { assertCase("2\\n1 -3\\n", "Alice\\n"); }
    @Test void case192() { assertCase("6\\n7 4 -1 0 17 1\\n", "Alice\\n"); }
    @Test void case193() { assertCase("3\\n0 1 1\\n", "Alice\\n"); }
    @Test void case194() { assertCase("2\\n1 11\\n", "Alice\\n"); }
    @Test void case195() { assertCase("6\\n7 4 0 1 17 5\\n", "Alice\\n"); }
    @Test void case196() { assertCase("3\\n5 1 0\\n", "Alice\\n"); }
    @Test void case197() { assertCase("2\\n-1 5\\n", "Alice\\n"); }
    @Test void case198() { assertCase("6\\n7 0 0 0 17 7\\n", "Alice\\n"); }
    @Test void case199() { assertCase("3\\n11 1 0\\n", "Alice\\n"); }
    @Test void case200() { assertCase("2\\n3 8\\n", "Alice\\n"); }
    @Test void case201() { assertCase("6\\n4 6 0 0 17 3\\n", "Bob\\n"); }
    @Test void case202() { assertCase("2\\n4 -1\\n", "Alice\\n"); }
    @Test void case203() { assertCase("6\\n7 4 1 0 17 5\\n", "Alice\\n"); }
    @Test void case204() { assertCase("3\\n9 0 -2\\n", "Alice\\n"); }
    @Test void case205() { assertCase("2\\n-2 1\\n", "Alice\\n"); }
}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1620_E. Replace the Numbers (manual I/O conversion)
        # ──────────────────────────────────────────────────────────────────────
        "id": "inventory_relabeling_stream_log112",
        "title": "Dynamic Inventory Management System",
        "class_name": "InventoryRelabelingStream",

        "signature": "public static String solve(String input)",

        "description": """\
You are designing a high-speed logging system for a warehouse inventory. The system tracks a linear catalog of item IDs, which starts empty. You need to process a series of `q` real-time instructions.

There are two types of instructions in the stream:
1. `1 x`: An item with ID `x` is added to the very end of the current catalog.
2. `2 x y`: A system-wide update occurs where every item currently in the catalog with ID `x` is relabeled to have the new ID `y`. 

Note: Relabeling only affects items currently present in the catalog at the moment the instruction is received. Future additions of ID `x` are not affected unless another type-2 instruction is issued.

After all instructions have been processed, generate a string representing the final state of the catalog from first to last item.

Input format:
- Line 1: An integer `q`, the number of instructions.
- Next `q` lines: Each contains an instruction in the format `1 x` or `2 x y`.

Output format:
- A single line containing the IDs in the final catalog, separated by spaces.

The solution must handle full input parsing and output formatting within the `solve(String input)` method.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class InventoryRelabelingStreamTest {

    private static String norm(String s) {
        if (s == null) return "";
        s = s.replace("\\r\\n", "\\n").replace("\\r", "\\n");
        String[] lines = s.split("\\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            int end = line.length();
            while (end > 0 && Character.isWhitespace(line.charAt(end - 1))) end--;
            sb.append(line, 0, end).append('\\n');
        }
        return sb.toString().trim();
    }

    private void assertCase(String input, String expected) {
        String actual = InventoryRelabelingStream.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    @Test void case001() { assertCase("8\\n2 1 4\\n1 1\\n1 4\\n1 2\\n2 2 4\\n2 4 3\\n1 2\\n2 2 7\\n", "1 3 3 7 \\n"); }
    @Test void case002() { assertCase("4\\n1 1\\n1 2\\n1 1\\n2 2 2\\n", "1 2 1 \\n"); }
    @Test void case003() { assertCase("7\\n1 3\\n1 1\\n2 1 2\\n1 2\\n1 1\\n1 2\\n2 1 3\\n", "3 2 2 3 2 \\n"); }
    @Test void case004() { assertCase("1\\n1 50\\n", "50 \\n"); }
    @Test void case005() { assertCase("1\\n1 114514\\n", "114514 \\n"); }
    @Test void case006() { assertCase("1\\n1 2002\\n", "2002 \\n"); }
    @Test void case007() { assertCase("1\\n1 500\\n", "500 \\n"); }
    @Test void case008() { assertCase("1\\n1 28\\n", "28"); }
    @Test void case009() { assertCase("1\\n1 2887\\n", "2887"); }
    @Test void case010() { assertCase("1\\n1 228\\n", "228"); }
    @Test void case011() { assertCase("1\\n1 29\\n", "29"); }
    @Test void case012() { assertCase("1\\n1 1270\\n", "1270"); }
    @Test void case013() { assertCase("1\\n1 182\\n", "182"); }
    @Test void case014() { assertCase("1\\n1 2279\\n", "2279"); }
    @Test void case015() { assertCase("1\\n1 979\\n", "979"); }
    @Test void case016() { assertCase("1\\n1 1719\\n", "1719"); }
    @Test void case017() { assertCase("1\\n1 1163\\n", "1163"); }
    @Test void case018() { assertCase("1\\n1 1134\\n", "1134"); }
    @Test void case019() { assertCase("1\\n1 2216\\n", "2216"); }
    @Test void case020() { assertCase("1\\n1 810\\n", "810"); }
    @Test void case021() { assertCase("1\\n1 1162\\n", "1162"); }
    @Test void case022() { assertCase("1\\n1 8\\n", "8"); }
    @Test void case023() { assertCase("1\\n1 176923\\n", "176923"); }
    @Test void case024() { assertCase("1\\n1 346\\n", "346"); }
    @Test void case025() { assertCase("8\\n2 2 4\\n1 1\\n1 4\\n1 2\\n2 2 4\\n2 4 3\\n1 2\\n2 2 7\\n", "1 3 3 7"); }
    @Test void case026() { assertCase("4\\n1 1\\n1 2\\n1 1\\n2 3 2\\n", "1 2 1"); }
    @Test void case027() { assertCase("7\\n1 3\\n1 1\\n2 1 2\\n1 2\\n1 1\\n1 1\\n2 1 3\\n", "3 2 2 3 3"); }
    @Test void case028() { assertCase("1\\n1 192\\n", "192"); }
    @Test void case029() { assertCase("1\\n1 6\\n", "6"); }
    @Test void case030() { assertCase("1\\n1 1566\\n", "1566"); }
    @Test void case031() { assertCase("1\\n1 1612\\n", "1612"); }
    @Test void case032() { assertCase("1\\n1 391\\n", "391"); }
    @Test void case033() { assertCase("1\\n1 1904\\n", "1904"); }
    @Test void case034() { assertCase("1\\n1 12\\n", "12"); }
    @Test void case035() { assertCase("1\\n1 455\\n", "455"); }
    @Test void case036() { assertCase("8\\n2 2 4\\n1 1\\n1 4\\n1 2\\n2 2 6\\n2 4 3\\n1 2\\n2 2 7\\n", "1 3 6 7"); }
    @Test void case037() { assertCase("4\\n1 2\\n1 2\\n1 1\\n2 3 2\\n", "2 2 1"); }
    @Test void case038() { assertCase("1\\n1 61\\n", "61"); }
    @Test void case039() { assertCase("1\\n1 3\\n", "3"); }
    @Test void case040() { assertCase("1\\n1 107\\n", "107"); }
    @Test void case041() { assertCase("1\\n1 537\\n", "537"); }
    @Test void case042() { assertCase("1\\n1 520\\n", "520"); }
    @Test void case043() { assertCase("1\\n1 72\\n", "72"); }
    @Test void case044() { assertCase("1\\n1 415\\n", "415"); }
    @Test void case045() { assertCase("1\\n1 639\\n", "639"); }
    @Test void case046() { assertCase("1\\n1 705\\n", "705"); }
    @Test void case047() { assertCase("1\\n1 34\\n", "34"); }
    @Test void case048() { assertCase("1\\n1 42\\n", "42"); }
    @Test void case049() { assertCase("1\\n1 91\\n", "91"); }
    @Test void case050() { assertCase("1\\n1 123055\\n", "123055"); }
    @Test void case051() { assertCase("1\\n1 408\\n", "408"); }
    @Test void case052() { assertCase("8\\n2 1 4\\n1 1\\n1 4\\n1 2\\n2 2 4\\n2 4 3\\n1 2\\n2 1 7\\n", "7 3 3 2"); }
    @Test void case053() { assertCase("1\\n1 10\\n", "10"); }
    @Test void case054() { assertCase("1\\n1 5175\\n", "5175"); }
    @Test void case055() { assertCase("1\\n1 37\\n", "37"); }
    @Test void case056() { assertCase("1\\n1 2219\\n", "2219"); }
    @Test void case057() { assertCase("1\\n1 205\\n", "205"); }
    @Test void case058() { assertCase("1\\n1 1536\\n", "1536"); }
    @Test void case059() { assertCase("1\\n1 1539\\n", "1539"); }
    @Test void case060() { assertCase("1\\n1 1784\\n", "1784"); }
    @Test void case061() { assertCase("1\\n1 147\\n", "147"); }
    @Test void case062() { assertCase("1\\n1 825\\n", "825"); }
    @Test void case063() { assertCase("1\\n1 3545\\n", "3545"); }
    @Test void case064() { assertCase("1\\n1 14\\n", "14"); }
    @Test void case065() { assertCase("7\\n1 3\\n1 1\\n2 1 1\\n1 2\\n1 1\\n1 1\\n2 1 3\\n", "3 3 2 3 3"); }
    @Test void case066() { assertCase("1\\n1 212\\n", "212"); }
    @Test void case067() { assertCase("1\\n1 416\\n", "416"); }
    @Test void case068() { assertCase("1\\n1 1055\\n", "1055"); }
    @Test void case069() { assertCase("1\\n1 341\\n", "341"); }
    @Test void case070() { assertCase("1\\n1 3564\\n", "3564"); }
    @Test void case071() { assertCase("1\\n1 5\\n", "5"); }
    @Test void case072() { assertCase("8\\n2 2 4\\n1 1\\n1 4\\n1 2\\n2 2 6\\n2 4 3\\n1 2\\n2 2 5\\n", "1 3 6 5"); }
    @Test void case073() { assertCase("1\\n1 1\\n", "1"); }
    @Test void case074() { assertCase("1\\n1 115\\n", "115"); }
    @Test void case075() { assertCase("1\\n1 727\\n", "727"); }
    @Test void case076() { assertCase("1\\n1 98\\n", "98"); }
    @Test void case077() { assertCase("1\\n1 55\\n", "55"); }
    @Test void case078() { assertCase("1\\n1 284\\n", "284"); }
    @Test void case079() { assertCase("1\\n1 4\\n", "4"); }
    @Test void case080() { assertCase("1\\n1 9\\n", "9"); }
    @Test void case081() { assertCase("1\\n1 583\\n", "583"); }
    @Test void case082() { assertCase("1\\n1 16\\n", "16"); }
    @Test void case083() { assertCase("1\\n1 2794\\n", "2794"); }
    @Test void case084() { assertCase("1\\n1 59\\n", "59"); }
    @Test void case085() { assertCase("1\\n1 300\\n", "300"); }
    @Test void case086() { assertCase("1\\n1 388\\n", "388"); }
    @Test void case087() { assertCase("1\\n1 1084\\n", "1084"); }
    @Test void case088() { assertCase("1\\n1 2314\\n", "2314"); }
    @Test void case089() { assertCase("1\\n1 736\\n", "736"); }
    @Test void case090() { assertCase("1\\n1 4527\\n", "4527"); }
    @Test void case091() { assertCase("1\\n1 2\\n", "2"); }
    @Test void case092() { assertCase("1\\n1 439\\n", "439"); }
    @Test void case093() { assertCase("1\\n1 86\\n", "86"); }
    @Test void case094() { assertCase("1\\n1 5588\\n", "5588"); }
    @Test void case095() { assertCase("1\\n1 152\\n", "152"); }
    @Test void case096() { assertCase("1\\n1 41\\n", "41"); }
    @Test void case097() { assertCase("1\\n1 260\\n", "260"); }
    @Test void case098() { assertCase("1\\n1 551\\n", "551"); }
    @Test void case099() { assertCase("1\\n1 2765\\n", "2765"); }
    @Test void case100() { assertCase("1\\n1 1371\\n", "1371"); }
    @Test void case101() { assertCase("1\\n1 127\\n", "127"); }
    @Test void case102() { assertCase("1\\n1 8623\\n", "8623"); }
    @Test void case103() { assertCase("1\\n1 49\\n", "49"); }
    @Test void case104() { assertCase("1\\n1 874\\n", "874"); }
    @Test void case105() { assertCase("1\\n1 376\\n", "376"); }
    @Test void case106() { assertCase("1\\n1 58\\n", "58"); }
    @Test void case107() { assertCase("1\\n1 6215\\n", "6215"); }
    @Test void case108() { assertCase("1\\n1 1464\\n", "1464"); }
    @Test void case109() { assertCase("1\\n1 33\\n", "33"); }
    @Test void case110() { assertCase("1\\n1 4800\\n", "4800"); }
    @Test void case111() { assertCase("1\\n1 6121\\n", "6121"); }
    @Test void case112() { assertCase("1\\n1 121267\\n", "121267"); }
    @Test void case113() { assertCase("1\\n1 3093\\n", "3093"); }
    @Test void case114() { assertCase("1\\n1 19\\n", "19"); }
    @Test void case115() { assertCase("1\\n1 202\\n", "202"); }
    @Test void case116() { assertCase("1\\n1 1050\\n", "1050"); }
    @Test void case117() { assertCase("1\\n1 2535\\n", "2535"); }
    @Test void case118() { assertCase("1\\n1 1306\\n", "1306"); }
    @Test void case119() { assertCase("1\\n1 1571\\n", "1571"); }
    @Test void case120() { assertCase("1\\n1 1578\\n", "1578"); }
    @Test void case121() { assertCase("1\\n1 142\\n", "142"); }
    @Test void case122() { assertCase("1\\n1 2055\\n", "2055"); }
    @Test void case123() { assertCase("1\\n1 53\\n", "53"); }
    @Test void case124() { assertCase("1\\n1 3184\\n", "3184"); }
    @Test void case125() { assertCase("1\\n1 21\\n", "21"); }
    @Test void case126() { assertCase("1\\n1 642\\n", "642"); }
    @Test void case127() { assertCase("1\\n1 15\\n", "15"); }
    @Test void case128() { assertCase("1\\n1 23\\n", "23"); }
    @Test void case129() { assertCase("1\\n1 169\\n", "169"); }
    @Test void case130() { assertCase("1\\n1 861\\n", "861"); }
    @Test void case131() { assertCase("1\\n1 139\\n", "139"); }
    @Test void case132() { assertCase("1\\n1 552\\n", "552"); }
    @Test void case133() { assertCase("1\\n1 247\\n", "247"); }
    @Test void case134() { assertCase("1\\n1 40\\n", "40"); }
    @Test void case135() { assertCase("1\\n1 46\\n", "46"); }
    @Test void case136() { assertCase("1\\n1 173\\n", "173"); }
    @Test void case137() { assertCase("1\\n1 171905\\n", "171905"); }
    @Test void case138() { assertCase("1\\n1 509\\n", "509"); }
    @Test void case139() { assertCase("1\\n1 7014\\n", "7014"); }
    @Test void case140() { assertCase("1\\n1 47\\n", "47"); }
    @Test void case141() { assertCase("1\\n1 335\\n", "335"); }
    @Test void case142() { assertCase("1\\n1 3035\\n", "3035"); }
    @Test void case143() { assertCase("1\\n1 237\\n", "237"); }
    @Test void case144() { assertCase("1\\n1 4338\\n", "4338"); }
    @Test void case145() { assertCase("7\\n1 6\\n1 1\\n2 1 1\\n1 2\\n1 1\\n1 1\\n2 1 3\\n", "6 3 2 3 3"); }
    @Test void case146() { assertCase("1\\n1 528\\n", "528"); }
    @Test void case147() { assertCase("1\\n1 1192\\n", "1192"); }
    @Test void case148() { assertCase("1\\n1 210\\n", "210"); }
    @Test void case149() { assertCase("1\\n1 1402\\n", "1402"); }
    @Test void case150() { assertCase("1\\n1 195\\n", "195"); }
    @Test void case151() { assertCase("1\\n1 347\\n", "347"); }
    @Test void case152() { assertCase("1\\n1 208\\n", "208"); }
    @Test void case153() { assertCase("1\\n1 525\\n", "525"); }
    @Test void case154() { assertCase("1\\n1 413\\n", "413"); }
    @Test void case155() { assertCase("1\\n1 4000\\n", "4000"); }
    @Test void case156() { assertCase("1\\n1 587\\n", "587"); }
    @Test void case157() { assertCase("1\\n1 6510\\n", "6510"); }
    @Test void case158() { assertCase("1\\n1 209\\n", "209"); }
    @Test void case159() { assertCase("1\\n1 430\\n", "430"); }
    @Test void case160() { assertCase("1\\n1 1080\\n", "1080"); }
    @Test void case161() { assertCase("1\\n1 56\\n", "56"); }
    @Test void case162() { assertCase("1\\n1 483\\n", "483"); }
    @Test void case163() { assertCase("1\\n1 12268\\n", "12268"); }
    @Test void case164() { assertCase("1\\n1 1439\\n", "1439"); }
    @Test void case165() { assertCase("1\\n1 9124\\n", "9124"); }
    @Test void case166() { assertCase("1\\n1 9067\\n", "9067"); }
    @Test void case167() { assertCase("1\\n1 34301\\n", "34301"); }
    @Test void case168() { assertCase("1\\n1 553\\n", "553"); }
    @Test void case169() { assertCase("1\\n1 35\\n", "35"); }
    @Test void case170() { assertCase("1\\n1 4704\\n", "4704"); }
    @Test void case171() { assertCase("1\\n1 994\\n", "994"); }
    @Test void case172() { assertCase("1\\n1 1751\\n", "1751"); }
    @Test void case173() { assertCase("1\\n1 702\\n", "702"); }
    @Test void case174() { assertCase("1\\n1 224\\n", "224"); }
    @Test void case175() { assertCase("4\\n1 1\\n1 1\\n1 1\\n2 6 2\\n", "1 1 1"); }
    @Test void case176() { assertCase("1\\n1 278\\n", "278"); }
    @Test void case177() { assertCase("1\\n1 70\\n", "70"); }
    @Test void case178() { assertCase("1\\n1 26\\n", "26"); }
    @Test void case179() { assertCase("1\\n1 99\\n", "99"); }
    @Test void case180() { assertCase("1\\n1 487\\n", "487"); }
    @Test void case181() { assertCase("1\\n1 502\\n", "502"); }
    @Test void case182() { assertCase("1\\n1 145712\\n", "145712"); }
    @Test void case183() { assertCase("1\\n1 4942\\n", "4942"); }
    @Test void case184() { assertCase("1\\n1 7\\n", "7"); }
    @Test void case185() { assertCase("1\\n1 2767\\n", "2767"); }
    @Test void case186() { assertCase("1\\n1 340\\n", "340"); }
    @Test void case187() { assertCase("1\\n1 8530\\n", "8530"); }
    @Test void case188() { assertCase("1\\n1 63\\n", "63"); }
    @Test void case189() { assertCase("1\\n1 1575\\n", "1575"); }
    @Test void case190() { assertCase("1\\n1 2756\\n", "2756"); }
    @Test void case191() { assertCase("1\\n1 821\\n", "821"); }
    @Test void case192() { assertCase("1\\n1 2667\\n", "2667"); }
    @Test void case193() { assertCase("1\\n1 25\\n", "25"); }
    @Test void case194() { assertCase("1\\n1 11\\n", "11"); }
    @Test void case195() { assertCase("1\\n1 2714\\n", "2714"); }
    @Test void case196() { assertCase("1\\n1 4721\\n", "4721"); }
    @Test void case197() { assertCase("1\\n1 369\\n", "369"); }
    @Test void case198() { assertCase("1\\n1 4188\\n", "4188"); }
    @Test void case199() { assertCase("1\\n1 103\\n", "103"); }
    @Test void case200() { assertCase("1\\n1 87\\n", "87"); }
    @Test void case201() { assertCase("1\\n1 18\\n", "18"); }
    @Test void case202() { assertCase("1\\n1 679\\n", "679"); }
    @Test void case203() { assertCase("1\\n1 423\\n", "423"); }
    @Test void case204() { assertCase("1\\n1 13\\n", "13"); }
    @Test void case205() { assertCase("1\\n1 2163\\n", "2163"); }
    @Test void case206() { assertCase("1\\n1 494\\n", "494"); }
    @Test void case207() { assertCase("1\\n1 223\\n", "223"); }
}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1613_E. Crazy Robot (manual I/O conversion)
        # Source  : hard_problems_with_testsFromCodeForces.jsonl
        # ──────────────────────────────────────────────────────────────────────
        "id": "crazy_robot_io_log112",

        "title": "Labyrinth Auto-Fill Robot",

        "class_name": "CrazyRobotIO",



        "signature": "public static String solve(String input)",



        "description": """\

Given a grid containing walls '#', empty cells '.', and exactly one robot

start cell 'L', determine every cell the robot can eventually reach.



Reachability rule: a non-wall cell becomes reachable if and only if

  (a) it is adjacent (4-directional) to an already-reachable cell, AND

  (b) among all of its non-wall neighbours, at most 1 is not yet reachable.



The robot's start cell 'L' is always reachable. Apply the rule repeatedly

(in any order) until no more cells can be added.



Output the grid with every newly reachable '.' replaced by '+'.

The 'L' cell and all '#' cells are printed unchanged.



The input may contain multiple test cases, each preceded by a line giving

the grid dimensions (rows and columns).



Implement full input parsing and output formatting in `solve(String input)`.

""",


        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class CrazyRobotIOTest {

    private static String norm(String s) {
        if (s == null) return "";
        s = s.replace("\\r\\n", "\\n").replace("\\r", "\\n");
        String[] lines = s.split("\\n", -1);
        StringBuilder sb = new StringBuilder();
        for (String line : lines) {
            int end = line.length();
            while (end > 0 && Character.isWhitespace(line.charAt(end - 1))) end--;
            sb.append(line, 0, end).append('\\n');
        }
        return sb.toString().trim();
    }

    private void assertCase(String input, String expected) {
        String actual = CrazyRobotIO.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    @Test void case001() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n....L..#.\\n", "...\\n.L.\\n...\\n#++++\\n..##L\\n...#+\\n...++\\nL\\n++++L++#.\\n"); }
    @Test void case002() { assertCase("1\\n3 31\\n############################..#\\n.............................L.\\n############################..#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case003() { assertCase("1\\n3 25\\n######################..#\\n.......................L.\\n######################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n######################++#\\n"); }
    @Test void case004() { assertCase("1\\n3 31\\n#############################..\\n.............................L.\\n############################..#\\n", "#############################++\\n+++++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case005() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n######################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case006() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "...\\n.L.\\n...\\n#++++\\n..##L\\n...#+\\n...++\\nL\\n.#++L++++\\n"); }
    @Test void case007() { assertCase("1\\n3 31\\n############################..#\\n.L.............................\\n############################..#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n############################..#\\n"); }
    @Test void case008() { assertCase("1\\n3 25\\n#..######################\\n.......................L.\\n######################..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n######################++#\\n"); }
    @Test void case009() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..######################\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case010() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..######################\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case011() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..######################\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case012() { assertCase("1\\n3 25\\n######################..#\\n.......................L.\\n#..######################\\n", "######################++#\\n...++++++++++++++++++++L+\\n#..######################\\n"); }
    @Test void case013() { assertCase("1\\n2 31\\n############################..#\\n.L.............................\\n############################..#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n"); }
    @Test void case014() { assertCase("1\\n3 25\\n######################..#\\n.L.......................\\n######################..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n######################..#\\n"); }
    @Test void case015() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n.#...\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "...\\n.L.\\n...\\n#++++\\n++##L\\n+#...\\n++...\\nL\\n.#++L++++\\n"); }
    @Test void case016() { assertCase("1\\n3 31\\n#..############################\\n.L.............................\\n############################..#\\n", "#++############################\\n+L++++++++++++++++++++++++++...\\n############################..#\\n"); }
    @Test void case017() { assertCase("1\\n3 25\\n#####################..##\\n.......................L.\\n#..######################\\n", "#####################..##\\n.......................L+\\n#..######################\\n"); }
    @Test void case018() { assertCase("4\\n3 3\\n...\\n..L\\n...\\n4 5\\n#....\\n..##L\\n.#...\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "..+\\n..L\\n..+\\n#++++\\n++##L\\n+#...\\n++...\\nL\\n.#++L++++\\n"); }
    @Test void case019() { assertCase("1\\n3 25\\n#####################..##\\n.L.......................\\n#..######################\\n", "#####################..##\\n+L+++++++++++++++++++....\\n#++######################\\n"); }
    @Test void case020() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n#################\\"##########..#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case021() { assertCase("1\\n3 31\\n..#############################\\n.............................L.\\n############################..#\\n", "..#############################\\n..+++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case022() { assertCase("1\\n3 25\\n#..######################\\n.L.......................\\n######################..#\\n", "#++######################\\n+L++++++++++++++++++++...\\n######################..#\\n"); }
    @Test void case023() { assertCase("1\\n3 25\\n##..#####################\\n.......................L.\\n#..######################\\n", "##..#####################\\n....+++++++++++++++++++L+\\n#..######################\\n"); }
    @Test void case024() { assertCase("1\\n3 31\\n#############################..\\n...........L...................\\n############################..#\\n", "#############################..\\n+++++++++++L++++++++++++++++...\\n############################..#\\n"); }
    @Test void case025() { assertCase("1\\n3 25\\n######################..#\\n.L.......................\\n#..######################\\n", "######################..#\\n+L++++++++++++++++++++...\\n#++######################\\n"); }
    @Test void case026() { assertCase("1\\n2 25\\n##.#############.########\\n.L.......................\\n#..###$###########$######\\n", "##.#############.########\\n+L.......................\\n"); }
    @Test void case027() { assertCase("1\\n3 31\\n#..############################\\n.L.............................\\n#..############################\\n", "#++############################\\n+L+++++++++++++++++++++++++++++\\n#++############################\\n"); }
    @Test void case028() { assertCase("1\\n3 25\\n##..#####################\\n.L.......................\\n#..######################\\n", "##..#####################\\n+L.......................\\n#++######################\\n"); }
    @Test void case029() { assertCase("1\\n3 31\\n#..############################\\n.............................L.\\n############################..#\\n", "#..############################\\n...++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case030() { assertCase("1\\n3 25\\n#..######################\\n.......................L.\\n#..######################\\n", "#..######################\\n...++++++++++++++++++++L+\\n#..######################\\n"); }
    @Test void case031() { assertCase("1\\n3 25\\n#####################..##\\n.L.......................\\n######################..#\\n", "#####################..##\\n+L+++++++++++++++++++....\\n######################..#\\n"); }
    @Test void case032() { assertCase("1\\n2 25\\n################.#####.##\\n.L.......................\\n#..######$####\\"#$########\\n", "################.#####.##\\n+L++++++++++++++.........\\n"); }
    @Test void case033() { assertCase("1\\n3 31\\n..#############################\\n.L.............................\\n############################..#\\n", "++#############################\\n+L++++++++++++++++++++++++++...\\n############################..#\\n"); }
    @Test void case034() { assertCase("1\\n2 31\\n#..############################\\n.............................L.\\n##########\\"######\\"##########./#\\n", "#..############################\\n...++++++++++++++++++++++++++L+\\n"); }
    @Test void case035() { assertCase("1\\n3 31\\n#############################..\\n...................L...........\\n############################..#\\n", "#############################..\\n+++++++++++++++++++L++++++++...\\n############################..#\\n"); }
    @Test void case036() { assertCase("1\\n3 31\\n#..############################\\n.L.............................\\n#.##.##########################\\n", "#++############################\\n+L++...........................\\n#+##.##########################\\n"); }
    @Test void case037() { assertCase("1\\n2 25\\n##.##########.###########\\n.L.......................\\n####\\"#################..#\\n", "##.##########.###########\\n+L.......................\\n"); }
    @Test void case038() { assertCase("1\\n2 25\\n##.#####.################\\n.......................L.\\n#############\\"########..#\\n", "##.#####.################\\n.........++++++++++++++L+\\n"); }
    @Test void case039() { assertCase("1\\n2 25\\n################.#####.##\\n.......................L.\\n######\\"######\\"##$#####..#\\n", "################.#####.##\\n.......................L+\\n"); }
    @Test void case040() { assertCase("1\\n3 31\\n#..############################\\n.L.............................\\n################.############.#\\n", "#++############################\\n+L++++++++++++++...............\\n################.############.#\\n"); }
    @Test void case041() { assertCase("4\\n3 3\\n...\\n..L\\n...\\n4 5\\n#....\\n..##L\\n..#..\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "..+\\n..L\\n..+\\n#++++\\n..##L\\n..#..\\n.....\\nL\\n.#++L++++\\n"); }
    @Test void case042() { assertCase("1\\n3 25\\n#..######################\\n.L.......................\\n#..######################\\n", "#++######################\\n+L+++++++++++++++++++++++\\n#++######################\\n"); }
    @Test void case043() { assertCase("1\\n3 31\\n#..############################\\n.............................L.\\n#..############################\\n", "#..############################\\n...++++++++++++++++++++++++++L+\\n#..############################\\n"); }
    @Test void case044() { assertCase("1\\n2 25\\n##.#####.################\\n.L.......................\\n#..######$####\\"#$########\\n", "##.#####.################\\n+L.......................\\n"); }
    @Test void case045() { assertCase("1\\n3 31\\n#..############################\\n.............................L.\\n#.##.##########################\\n", "#..############################\\n.....++++++++++++++++++++++++L+\\n#.##.##########################\\n"); }
    @Test void case046() { assertCase("1\\n2 25\\n######################..#\\n......................L..\\n#..###$##################\\n", "######################++#\\n++++++++++++++++++++++L++\\n"); }
    @Test void case047() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n.#...\\n.....\\n1 1\\nL\\n1 9\\n....L..#.\\n", "...\\n.L.\\n...\\n#++++\\n++##L\\n+#...\\n++...\\nL\\n++++L++#.\\n"); }
    @Test void case048() { assertCase("1\\n2 25\\n#####################..##\\n.......................L.\\n#..######################\\n", "#####################..##\\n.......................L+\\n"); }
    @Test void case049() { assertCase("1\\n2 25\\n########.#############.##\\n.L.......................\\n#..###$###########$######\\n", "########.#############.##\\n+L++++++.................\\n"); }
    @Test void case050() { assertCase("1\\n2 25\\n###########.##########.##\\n.L.......................\\n####\\"#################..#\\n", "###########.##########.##\\n+L+++++++++..............\\n"); }
    @Test void case051() { assertCase("1\\n3 31\\n#..############################\\n.............................L.\\n################.############.#\\n", "#..############################\\n.................++++++++++++L+\\n################.############+#\\n"); }
    @Test void case052() { assertCase("1\\n2 25\\n##########.############.#\\n......................L..\\n#..###$##################\\n", "##########.############.#\\n...........+++++++++++L..\\n"); }
    @Test void case053() { assertCase("1\\n2 31\\n#..############################\\n...............L...............\\n#/.##########\\"######\\"##########\\n", "#..############################\\n...++++++++++++L+++++++++++++++\\n"); }
    @Test void case054() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\nL.##.\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n....L..#.\\n", "...\\n.L.\\n...\\n#....\\nL.##.\\n...#.\\n.....\\nL\\n++++L++#.\\n"); }
    @Test void case055() { assertCase("1\\n2 31\\n#############################..\\n.............................L.\\n############################..#\\n", "#############################++\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case056() { assertCase("4\\n3 3\\n...\\n..L\\n...\\n4 5\\n#....\\n..##L\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "..+\\n..L\\n..+\\n#++++\\n..##L\\n...#+\\n...++\\nL\\n.#++L++++\\n"); }
    @Test void case057() { assertCase("1\\n2 25\\n#..######################\\n....................L....\\n#..######################\\n", "#..######################\\n...+++++++++++++++++L++++\\n"); }
    @Test void case058() { assertCase("1\\n2 25\\n##..#####################\\n.L.......................\\n#..######################\\n", "##..#####################\\n+L.......................\\n"); }
    @Test void case059() { assertCase("1\\n2 31\\n..#############################\\n.............................L.\\n############################..#\\n", "..#############################\\n..+++++++++++++++++++++++++++L+\\n"); }
    @Test void case060() { assertCase("1\\n3 25\\n##..#####################\\n.L.......................\\n######################..#\\n", "##..#####################\\n+L.......................\\n######################..#\\n"); }
    @Test void case061() { assertCase("1\\n3 31\\n#############################..\\n...................L...........\\n#..############################\\n", "#############################..\\n...++++++++++++++++L+++++++++..\\n#..############################\\n"); }
    @Test void case062() { assertCase("1\\n2 25\\n######.###############.##\\n.......................L.\\n#..###$##################\\n", "######.###############.##\\n.......................L+\\n"); }
    @Test void case063() { assertCase("1\\n3 31\\n############################..#\\n.............................L.\\n#..############################\\n", "############################++#\\n...++++++++++++++++++++++++++L+\\n#..############################\\n"); }
    @Test void case064() { assertCase("1\\n2 31\\n#..############################\\n.L.............................\\n#################\\"##########-.#\\n", "#++############################\\n+L+++++++++++++++++++++++++++++\\n"); }
    @Test void case065() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..######################\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case066() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n######################..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case067() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###########\\"##########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case068() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n######################..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case069() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n######################..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case070() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..###$##################\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case071() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"#################..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case072() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..###$###########$######\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case073() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###$###########$######\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case074() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..#################\\"####\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case075() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n###########\\"##########..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case076() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###########\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case077() { assertCase("1\\n2 31\\n############################..#\\n.L.............................\\n#################\\"##########..#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n"); }
    @Test void case078() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"##############$##..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case079() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#################\\"####\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case080() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..##########\\"###########\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case081() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###########\\"#$####$###\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case082() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"###########$##$##..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case083() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#.#############.#########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case084() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..###$##################\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case085() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..####$############\\"####\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case086() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..######$####\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case087() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$#####$####\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case088() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..###############\\"######\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case089() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###$########$##$######\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case090() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"#######\\"######$##..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case091() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"###########$##$##..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case092() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n##################$###..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case093() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n##########\\"######\\"##########..#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case094() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$#####$#\\"##\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case095() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"#######\\"######$##..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case096() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n##################$###..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case097() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n##########\\"######\\"##########./#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case098() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..$#####$#\\"##\\"#$########\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case099() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n##############\\"#######..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case100() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n####\\"#################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case101() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..#####$#####\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case102() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..##$##$###########\\"####\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case103() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..####$############\\"####\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case104() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..###############!######\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case105() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n##################$###..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case106() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"#######\\"######$$#..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case107() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$#######\\"##\\"#$#####$##\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case108() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n####\\"#################..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case109() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n########$#\\"#####$#####..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case110() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n$#######$#\\"#####$#####..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case111() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###################$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case112() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#./######################\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case113() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#############\\"########..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case114() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n########$#\\"###########..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case115() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"##########\\"##########..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case116() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n#################\\"##########-.#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case117() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..$#####$####\\"#$########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case118() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###$########$##$######\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case119() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"####\\"#########$##..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case120() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n##$#\\"###########$##$##..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case121() { assertCase("1\\n2 31\\n############################..#\\n.L.............................\\n##########\\"######\\"##########..#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n"); }
    @Test void case122() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..$#####$#\\"##\\"#$########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case123() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n\\"###\\"#################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case124() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..####$############\\"\\"###\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case125() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n######!###############..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case126() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###$##################\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case127() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"#################..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case128() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###########\\"#######$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case129() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#############\\"########..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case130() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n#.-##########\\"#################\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case131() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n######$##$########$###..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case132() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"####\\"#########$##..\\"\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case133() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#################\\"###\\"\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case134() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#\\"#########\\"#######$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case135() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"####\\"##$######$##..\\"\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case136() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n\\"###\\"#########$#######..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case137() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#\\"#########\\"###\\"###$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case138() { assertCase("1\\n2 25\\n##.#####.################\\n.......................L.\\n#############\\"##$#####..#\\n", "##.#####.################\\n.........++++++++++++++L+\\n"); }
    @Test void case139() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#######$#########\\"###\\"\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case140() { assertCase("1\\n2 25\\n##.#####.################\\n.......................L.\\n######\\"######\\"##$#####..#\\n", "##.#####.################\\n.........++++++++++++++L+\\n"); }
    @Test void case141() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..#######$#####\\"###\\"###\\"\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case142() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n\\"###\\"###\\"#####$#######..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case143() { assertCase("1\\n2 25\\n################.#####.##\\n.L.......................\\n######\\"######\\"##$#####..#\\n", "################.#####.##\\n+L++++++++++++++.........\\n"); }
    @Test void case144() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###########\\"##########\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case145() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"###########$#####..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case146() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###$######\\"####$######\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case147() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..#######\\"#########\\"####\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case148() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#.#############.#########\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case149() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###$########%##$######\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case150() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"###########$##$##..$\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case151() { assertCase("1\\n2 31\\n############################..#\\n.L.............................\\n#..##########\\"######\\"##########\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n"); }
    @Test void case152() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$#####$$\\"##\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case153() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..$#####$#\\"##\\"#######$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case154() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n##############\\"#######..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case155() { assertCase("1\\n2 25\\n##.#############.########\\n.L.......................\\n#/.###$###########$######\\n", "##.#############.########\\n+L.......................\\n"); }
    @Test void case156() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$#######\\"##\\"#$####\\"$##\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case157() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..###################$##\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case158() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#./######################\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case159() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####$########\\"########..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case160() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n###$####$#\\"###########..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case161() { assertCase("1\\n2 31\\n############################..#\\n.L.............................\\n#################\\"##########-.#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n"); }
    @Test void case162() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..$##\\"##$####\\"#$########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case163() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#./$#####$#\\"##\\"#$########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case164() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..####$############\\"\\"###\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case165() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"..##$#########\\"####\\"####\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case166() { assertCase("1\\n2 25\\n##.##########.###########\\n.L.......................\\n####\\"############\\"####..#\\n", "##.##########.###########\\n+L.......................\\n"); }
    @Test void case167() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"###\\"#########$#######..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case168() { assertCase("1\\n2 25\\n##.#####.################\\n.......................L.\\n#############\\"##%#####..#\\n", "##.#####.################\\n.........++++++++++++++L+\\n"); }
    @Test void case169() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"###\\"###\\"#####$#######..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case170() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..#######\\"#########\\"####\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case171() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n########$#\\"##\\"$$#####$..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case172() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n######\\"#######\\"#######..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case173() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..$###\\"###\\"##\\"#$####\\"$##\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case174() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#./$#####$#\\"##\\"#$#####$##\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case175() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"###\\"#$#######$#######..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case176() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..$###\\"###\\"##\\"#$####\\"$##\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case177() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n###\\"\\"#################..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case178() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n########$#\\"####$######..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case179() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n####\\"#########\\"####$##..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case180() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n##################$##\\"..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case181() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"#######\\"######$#$..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case182() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n####\\"#################..$\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case183() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..#####$$####\\"#$########\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case184() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n.#################$####.#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case185() { assertCase("1\\n2 25\\n################.#####.##\\n.L.......................\\n########$#\\"####$######..#\\n", "################.#####.##\\n+L++++++++++++++.........\\n"); }
    @Test void case186() { assertCase("1\\n2 31\\n#..############################\\n.............................L.\\n#/.##########\\"######\\"##########\\n", "#..############################\\n...++++++++++++++++++++++++++L+\\n"); }
    @Test void case187() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n\\"###\\"#################..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case188() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..###$######$###########\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case189() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"######\\"##########..#\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case190() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#############\\"$#######..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case191() { assertCase("1\\n2 31\\n############################..#\\n.............................L.\\n#.-######\\"#####################\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n"); }
    @Test void case192() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..#################\\"###\\"\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case193() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n\\"#############$#######..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case194() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n#..#######$#########\\"###\\"\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case195() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n#..###########!##########\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case196() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#.############$.#########\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case197() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n######$##%########$###..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
    @Test void case198() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n####\\"###########$#$###..$\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case199() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n#..$\\"#\\"##$####\\"#$########\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case200() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n#..####$###$########\\"\\"###\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case201() { assertCase("1\\n2 25\\n#..######################\\n.......................L.\\n\\"#$#\\"#########$#######..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n"); }
    @Test void case202() { assertCase("1\\n2 25\\n#..######################\\n.L.......................\\n$..#######\\"#########\\"####\\n", "#++######################\\n+L+++++++++++++++++++++++\\n"); }
    @Test void case203() { assertCase("1\\n2 25\\n######################..#\\n.L.......................\\n########$###\\"\\"$$#####$..#\\n", "######################..#\\n+L++++++++++++++++++++...\\n"); }
}
""",
    },
]


def get_problem(problem_id: str) -> dict:
    for p in PROBLEMS:
        if p["id"] == problem_id:
            return p
    raise KeyError(f"Unknown problem '{problem_id}'. Available: {[p['id'] for p in PROBLEMS]}")


def list_problems() -> list[dict]:
    return [{"id": p["id"], "title": p["title"]} for p in PROBLEMS]