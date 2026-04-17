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
        "id": "array_optimization_deque",
        "title": "Array Optimization by Deque",
        "class_name": "ArrayOptimizationDeque",

        "signature": "public static String solve(String input)",

        "description": """\
For each test case, you are given numbers `a1..an` in fixed arrival order.
You start with an empty double-ended queue.

When processing `ai`, you must place it either:
  - at the left end, or
  - at the right end.

After all insertions, evaluate how "unsorted" the final deque is.
The score is the count of pairs `(i, j)` such that:
  - `i < j` (position in the final deque), and
  - `d[i] > d[j]`.

Choose left/right placements to make this score as small as possible.

Input format:
  Line 1: t (number of test cases, 1 ≤ t ≤ 1000)
  For each test case:
    Line 1: n (1 ≤ n ≤ 2·10^5)
    Line 2: n space-separated integers a_i (-10^9 ≤ a_i ≤ 10^9)
  Sum of n over all test cases ≤ 2·10^5.

Output format:
  Print one integer per test case: the minimum achievable score.

Implement full parsing and output formatting in `solve(String input)`.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ArrayOptimizationDequeTest {

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
        String actual = ArrayOptimizationDeque.solve(input);
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
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Relay Window Shift Planning

        # ──────────────────────────────────────────────────────────────────────
        "id": "relay_window_shift",
        "title": "Relay Window Shift Planning",
        "class_name": "RelayWindowShift",

        "signature": "public static int minRelaysToShift(int n, int cycleLength, int[] offlineSlot, int[][] mirroredPairs)",

        "description": """\
A distributed relay network has `n` relays, indexed 1..n.

Each relay is briefly offline once per cycle of `cycleLength` slots.
Relay `j` is offline during slot `offlineSlot[j-1]` (0-based).

Each payload is mirrored on exactly two relays. If those two relays are
offline in the same slot, that payload becomes unavailable.
The given schedule is initially safe.

Engineers want to run an experiment:
- choose a non-empty subset of relays;
- shift each chosen relay's offline slot forward by exactly 1 (mod cycleLength).

After the shift, the schedule must still be safe for every mirrored pair.

Return the minimum possible number of chosen relays.

Input notes:
- Each `mirroredPairs[i]` has form `[a, b]` with 1-based indices and `a != b`.

Constraints:
- 2 <= n <= 100000
- 1 <= mirroredPairs.length <= 100000
- 2 <= cycleLength <= 100000
- 0 <= offlineSlot[j] < cycleLength
- Initial schedule is valid for all pairs.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import java.time.Duration;

class RelayWindowShiftTest {

    private int bruteMin(int n, int h, int[] u, int[][] pairs) {
        int best = Integer.MAX_VALUE;
        int totalMasks = 1 << n;
        for (int mask = 1; mask < totalMasks; mask++) {
            if (Integer.bitCount(mask) >= best) continue;
            if (isSafeAfterShift(mask, n, h, u, pairs)) {
                best = Integer.bitCount(mask);
            }
        }
        return best;
    }

    private boolean isSafeAfterShift(int mask, int n, int h, int[] u, int[][] pairs) {
        int[] shifted = new int[n];
        for (int i = 0; i < n; i++) {
            if (((mask >> i) & 1) == 1) shifted[i] = (u[i] + 1) % h;
            else shifted[i] = u[i];
        }
        for (int[] p : pairs) {
            int a = p[0] - 1, b = p[1] - 1;
            if (shifted[a] == shifted[b]) return false;
        }
        return true;
    }

    @Test void simpleCaseAnswerOne() {
        int n = 5, h = 9;
        int[] u = {0, 1, 3, 6, 8};
        int[][] p = {{1, 2}, {2, 3}, {3, 4}, {4, 5}};
        assertEquals(1, RelayWindowShift.minRelaysToShift(n, h, u, p));
    }

    @Test void connectedBidirectionalNeedsAll() {
        int n = 4, h = 2;
        int[] u = {0, 1, 0, 1};
        int[][] p = {{1, 2}, {2, 3}, {3, 4}};
        assertEquals(4, RelayWindowShift.minRelaysToShift(n, h, u, p));
    }

    @Test void wrapAroundInteraction() {
        int n = 6, h = 5;
        int[] u = {4, 0, 2, 3, 1, 4};
        int[][] p = {{1, 2}, {2, 3}, {3, 4}, {4, 5}, {5, 6}};
        int expected = bruteMin(n, h, u, p);
        assertEquals(expected, RelayWindowShift.minRelaysToShift(n, h, u, p));
    }

    @Test void multipleSmallCrossChecks() {
        int[][] casesU = {
            {0, 2, 4, 1, 3},
            {1, 4, 0, 3, 2},
            {2, 0, 3, 1, 4},
            {3, 1, 4, 2, 0}
        };
        int[][][] casesP = {
            {{1,2},{2,3},{3,4},{4,5}},
            {{1,3},{2,4},{3,5},{1,5}},
            {{1,2},{2,4},{4,5},{3,5}},
            {{1,4},{2,5},{1,3},{3,4}}
        };

        int h = 5;
        for (int i = 0; i < casesU.length; i++) {
            int[] u = casesU[i];
            int[][] p = casesP[i];
            int expected = bruteMin(5, h, u, p);
            int actual = RelayWindowShift.minRelaysToShift(5, h, u, p);
            assertEquals(expected, actual);
        }
    }

    @Test void exhaustiveOnTinyInstances() {
        int n = 6, h = 4;
        int[][] pairs = {{1,2},{2,3},{3,4},{4,5},{5,6},{1,6}};

        int limit = 1;
        for (int i = 0; i < n; i++) limit *= h;

        for (int mask = 0; mask < limit; mask++) {
            int x = mask;
            int[] u = new int[n];
            for (int i = 0; i < n; i++) {
                u[i] = x % h;
                x /= h;
            }

            boolean valid = true;
            for (int[] p : pairs) {
                if (u[p[0]-1] == u[p[1]-1]) { valid = false; break; }
            }
            if (!valid) continue;

            int expected = bruteMin(n, h, u, pairs);
            int actual = RelayWindowShift.minRelaysToShift(n, h, u, pairs);
            assertEquals(expected, actual);
        }
    }

    @Test void performanceLargeShouldBeNearLinear() {
        assertTimeoutPreemptively(Duration.ofSeconds(2), () -> {
            int n = 100000;
            int h = 200000;
            int[] u = new int[n];
            for (int i = 0; i < n; i++) u[i] = i;
            int[][] p = new int[n - 1][2];
            for (int i = 1; i < n; i++) {
                p[i - 1][0] = i;
                p[i - 1][1] = i + 1;
            }
            assertEquals(1, RelayWindowShift.minRelaysToShift(n, h, u, p));
        });
    }
}
""",
    },

    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Tree Queries (Codeforces 1606F)
        # Source  : deepmind/code_contests  |  difficulty 12  |  201 tests
        # ──────────────────────────────────────────────────────────────────────
        "id": "tree_queries",
        "title": "Tree Queries",
        "class_name": "TreeQueries",

        "signature": "public static long[] treeQueries(int n, int[][] edges, int[][] queries)",

        "description": """\
You are given a rooted tree of `n` vertices (1-indexed, rooted at vertex 1).
You must answer `q` independent queries.

For query (v, k):
  You may delete any vertices from the tree in any order, except the root (1)
  and the queried vertex v. When a vertex is deleted, its children are
  re-attached directly to its parent.

  Maximize the score:  c(v) - m * k
  where c(v) is the number of direct children of v after all deletions,
  and m is the total number of deleted vertices.

  Each query is independent — deletions in one query do not affect others.

Return an array of length q with the maximum score for each query.

Constraints:
  - 1 <= n <= 200000
  - 1 <= q <= 200000
  - 1 <= v <= n  (v may equal 1)
  - 0 <= k <= 200000
  - The input edges form a valid undirected tree.

Input format (for reference):
  Line 1 : n
  Lines 2..n : x y   (undirected edge)
  Line n+1 : q
  Lines n+2..n+1+q : v k

Output format:
  q integers, one per line.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.assertTimeoutPreemptively;
import java.time.Duration;
import java.util.*;

class TreeQueriesTest {

    // ── helpers ───────────────────────────────────────────────────────────────

    /** Brute-force: try all subsets of non-root, non-v vertices and pick best. */
    private long bruteForce(int n, int[][] edges, int v, int k) {
        // Build adjacency list
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i <= n; i++) adj.add(new ArrayList<>());
        for (int[] e : edges) { adj.get(e[0]).add(e[1]); adj.get(e[1]).add(e[0]); }

        // Candidates to delete: all vertices except root(1) and v
        List<Integer> cands = new ArrayList<>();
        for (int i = 1; i <= n; i++) if (i != 1 && i != v) cands.add(i);

        long best = Long.MIN_VALUE;
        int total = 1 << cands.size();
        for (int mask = 0; mask < total; mask++) {
            Set<Integer> deleted = new HashSet<>();
            for (int b = 0; b < cands.size(); b++)
                if (((mask >> b) & 1) == 1) deleted.add(cands.get(b));

            // Build contracted tree
            Map<Integer, List<Integer>> ct = new HashMap<>();
            for (int i = 1; i <= n; i++) if (!deleted.contains(i)) ct.put(i, new ArrayList<>());
            // BFS from root on original tree, skip deleted, attach survivors to nearest live ancestor
            int[] parent = new int[n + 1];
            Arrays.fill(parent, -1);
            Queue<Integer> bfs = new LinkedList<>();
            bfs.add(1);
            parent[1] = 0;
            while (!bfs.isEmpty()) {
                int cur = bfs.poll();
                for (int nb : adj.get(cur)) {
                    if (parent[nb] == -1 && nb != 1) {
                        parent[nb] = cur;
                        if (deleted.contains(nb)) {
                            // pass grandparent down
                            parent[nb] = parent[cur];
                        }
                        // find live parent
                        int liveP = deleted.contains(nb) ? parent[nb] : cur;
                        if (!deleted.contains(nb)) ct.get(liveP).add(nb);
                        bfs.add(nb);
                    }
                }
            }
            // simpler: recount children of v in contracted tree
            // count children of v: vertices whose live-parent is v
            int children = 0;
            for (int i = 1; i <= n; i++) {
                if (deleted.contains(i) || i == v) continue;
                // find live parent by walking up
                int cur = i;
                int par = parent[cur];
                while (par > 0 && deleted.contains(par)) par = parent[par];
                if (par == v) children++;
            }
            long score = (long) children - (long) deleted.size() * k;
            if (score > best) best = score;
        }
        return best;
    }

    // ── official example (from Codeforces 1606F) ─────────────────────────────

    @Test void DatasetCase01() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,1},{5,0},{7,200000}};
        long[] expected = {5, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase02() {
        // Same edges; query on v=7 with k=0 allows pulling all ancestors in
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,0},{5,1},{7,200000}};
        long[] expected = {5, 2, 1, 5, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase03() {
        // Edge between 8 and 3 replaced with edge between 8 and 2
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,2},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,6},{7,0},{5,1},{7,200000}};
        long[] expected = {4, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    // ── exact dataset tests from hard_problems_with_testsFromCodeForces.jsonl ────────────────────────────────
    @Test void DatasetCase04() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,1},{5,1},{7,200000}};
        long[] expected = {5, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase05() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{3,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,1},{5,0},{7,200000}};
        long[] expected = {5, 1, 1, 4, 0, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase06() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,3},{1,3},{7,0},{5,1},{7,200000}};
        long[] expected = {5, 1, 1, 5, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase07() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,2},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{2,0},{1,2},{1,6},{7,0},{5,1},{7,200000}};
        long[] expected = {1, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase08() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{5,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,0},{5,1},{7,200000}};
        long[] expected = {4, 1, 1, 4, 1, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase09() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,1},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,1},{8,1},{4,200000}};
        long[] expected = {5, 3, 2, 4, 0, 0};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase10() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,1},{5,7},{6,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,6},{7,0},{1,1},{7,200000}};
        long[] expected = {4, 2, 2, 3, 3, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase11() {
        int n = 8;
        int[][] edges = {{6,8},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{2,2},{1,3},{7,2},{5,0},{7,200000}};
        long[] expected = {4, 0, 1, 3, 0, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void DatasetCase12() {
        int n = 8;
        int[][] edges = {{6,7},{3,1},{8,2},{5,7},{7,4},{2,1},{7,3}};
        int[][] queries = {{2,0},{1,2},{2,3},{5,0},{3,1},{7,200000}};
        long[] expected = {1, 2, 1, 0, 2, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }, queries));
    }

    @Test void DatasetCase13() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,2},{5,7},{7,4},{4,1},{7,3}};
        int[][] queries = {{2,0},{1,1},{1,3},{7,0},{5,1},{7,200000}};
        long[] expected = {1, 1, 1, 3, 0, 3};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges

    // Performance check on the chosen hardest single dataset (Case 01). Limit is 6 seconds by rules
    @Test void performanceSixSecondRule() {
        assertTimeoutPreemptively(Duration.ofSeconds(6), () -> {
            int n = 8;
            int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
            int[][] queries = {{1,0},{1,2},{1,3},{7,1},{5,0},{7,200000}};
            long[] expected = {5, 2, 1, 4, 0, 4};
            long[] result = TreeQueries.treeQueries(n, edges, queries);
            assertArrayEquals(expected, result);
        });
    }

}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: Deque End-Pick Game
        #        Original: Codeforces 1600E - Array Game

        # ──────────────────────────────────────────────────────────────────────
        "id": "array_game_io",
        "title": "Deque End-Pick Game",
        "class_name": "ArrayGameIO",

        "signature": "public static String solve(String input)",

        "description": """\
Alice and Bob play a game on an array of N integers.
They take turns, with Alice going first. On each turn the current player
must pick exactly one value from either the left end or the right end of
the remaining array. The picked value is removed from the array.

The sequence of all values picked so far (across both players, in order)
must remain strictly increasing after every pick. A player who cannot make
a valid move loses; the other player wins.

Both players play optimally. Determine who wins.

Input format:
  Line 1: N
  Line 2: N space-separated integers

Output format:
  One line: "Alice" or "Bob"

Implement full parsing and output formatting in `solve(String input)`.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ArrayGameIOTest {

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
        String actual = ArrayGameIO.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    @Test void case01() { assertCase("6\\n5 8 2 1 10 9\\n", "Bob\\n"); }
    @Test void case02() { assertCase("3\\n5 4 5\\n", "Alice\\n"); }
    @Test void case03() { assertCase("1\\n5\\n", "Alice\\n"); }
    @Test void case04() { assertCase("3\\n5 6 5\\n", "Bob\\n"); }
    @Test void case05() { assertCase("2\\n5 12\\n", "Alice\\n"); }
    @Test void case06() { assertCase("3\\n5 6 9\\n", "Alice\\n"); }
    @Test void case07() { assertCase("6\\n2 6 0 0 5 0\\n", "Bob\\n"); }
    @Test void case08() { assertCase("2\\n5 2\\n", "Alice\\n"); }
    @Test void case09() { assertCase("6\\n5 4 2 1 10 9\\n", "Alice\\n"); }
    @Test void case10() { assertCase("3\\n5 1 5\\n", "Alice\\n"); }
    @Test void case11() { assertCase("1\\n2\\n", "Alice\\n"); }
    @Test void case12() { assertCase("3\\n5 6 10\\n", "Alice\\n"); }
    @Test void case13() { assertCase("2\\n5 3\\n", "Alice\\n"); }
    @Test void case14() { assertCase("6\\n4 4 2 1 10 9\\n", "Alice\\n"); }
    @Test void case15() { assertCase("3\\n7 1 5\\n", "Alice\\n"); }
    @Test void case16() { assertCase("1\\n3\\n", "Alice\\n"); }
}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1620_E. Replace the Numbers (manual I/O conversion)
        # ──────────────────────────────────────────────────────────────────────
        "id": "replace_numbers_io",
        "title": "Bulk Value Substitution Stream",
        "class_name": "ReplaceNumbersIO",

        "signature": "public static String solve(String input)",

        "description": """\
Maintain a sequence that starts empty and supports two query types:
1) `1 x`: append `x` to the end of the sequence.
2) `2 x y`: replace every current occurrence of `x` with `y`.

After processing all queries, print the final sequence.

Implement full input parsing and output formatting in `solve(String input)`.
The output format must match the original problem exactly.
""",

        "junit_test": """\
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ReplaceNumbersIOTest {

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
        String actual = ReplaceNumbersIO.solve(input);
        assertEquals(norm(expected), norm(actual));
    }

    @Test void case01() { assertCase("8\\n2 1 4\\n1 1\\n1 4\\n1 2\\n2 2 4\\n2 4 3\\n1 2\\n2 2 7\\n", "1 3 3 7 \\n"); }
    @Test void case02() { assertCase("4\\n1 1\\n1 2\\n1 1\\n2 2 2\\n", "1 2 1 \\n"); }
    @Test void case03() { assertCase("7\\n1 3\\n1 1\\n2 1 2\\n1 2\\n1 1\\n1 2\\n2 1 3\\n", "3 2 2 3 2 \\n"); }
    @Test void case04() { assertCase("1\\n1 50\\n", "50 \\n"); }
    @Test void case05() { assertCase("1\\n1 114514\\n", "114514 \\n"); }
    @Test void case06() { assertCase("1\\n1 2002\\n", "2002 \\n"); }
    @Test void case07() { assertCase("8\\n2 2 4\\n1 1\\n1 4\\n1 2\\n2 2 4\\n2 4 3\\n1 2\\n2 2 7\\n", "1 3 3 7"); }
    @Test void case08() { assertCase("4\\n1 1\\n1 2\\n1 1\\n2 3 2\\n", "1 2 1"); }
    @Test void case09() { assertCase("7\\n1 3\\n1 1\\n2 1 2\\n1 2\\n1 1\\n1 1\\n2 1 3\\n", "3 2 2 3 3"); }
}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1613_E. Crazy Robot (manual I/O conversion)
        # Source  : hard_problems_with_testsFromCodeForces.jsonl
        # ──────────────────────────────────────────────────────────────────────
        "id": "crazy_robot_io",
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

    @Test void case01() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n....L..#.\\n", "...\\n.L.\\n...\\n#++++\\n..##L\\n...#+\\n...++\\nL\\n++++L++#.\\n"); }
    @Test void case02() { assertCase("1\\n3 31\\n############################..#\\n.............................L.\\n############################..#\\n", "############################++#\\n+++++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case03() { assertCase("1\\n3 25\\n######################..#\\n.......................L.\\n######################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n######################++#\\n"); }
    @Test void case04() { assertCase("1\\n3 31\\n#############################..\\n.............................L.\\n############################..#\\n", "#############################++\\n+++++++++++++++++++++++++++++L+\\n############################++#\\n"); }
    @Test void case05() { assertCase("1\\n2 25\\n######################..#\\n.......................L.\\n######################..#\\n", "######################++#\\n+++++++++++++++++++++++L+\\n"); }
    @Test void case06() { assertCase("4\\n3 3\\n...\\n.L.\\n...\\n4 5\\n#....\\n..##L\\n...#.\\n.....\\n1 1\\nL\\n1 9\\n.#..L....\\n", "...\\n.L.\\n...\\n#++++\\n..##L\\n...#+\\n...++\\nL\\n.#++L++++\\n"); }
    @Test void case07() { assertCase("1\\n3 31\\n############################..#\\n.L.............................\\n############################..#\\n", "############################..#\\n+L++++++++++++++++++++++++++...\\n############################..#\\n"); }
    @Test void case08() { assertCase("1\\n3 25\\n#..######################\\n.......................L.\\n######################..#\\n", "#..######################\\n...++++++++++++++++++++L+\\n######################++#\\n"); }
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
