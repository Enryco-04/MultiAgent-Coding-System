"""
problems/problem_bank.py
-------------------------
APPS benchmark problems adapted to Java + JUnit 5.
"""

PROBLEMS = [
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

    @Test void officialExample() {
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,1},{5,0},{7,200000}};
        long[] expected = {5, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void officialExampleVariantA() {
        // Same tree, query 4 uses k=0 (v=7) → all ancestors pull in, expect 5
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,3},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,3},{7,0},{5,1},{7,200000}};
        long[] expected = {5, 2, 1, 5, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    @Test void officialExampleVariantB() {
        // Edge 8-3 replaced with 8-2; restructures the subtree
        int n = 8;
        int[][] edges = {{6,7},{3,2},{8,2},{5,7},{7,4},{7,1},{7,3}};
        int[][] queries = {{1,0},{1,2},{1,6},{7,0},{5,1},{7,200000}};
        long[] expected = {4, 2, 1, 4, 0, 4};
        assertArrayEquals(expected, TreeQueries.treeQueries(n, edges, queries));
    }

    // ── leaf node is always 0 regardless of k ────────────────────────────────

    @Test void leafQueryAlwaysZero() {
        // Path graph 1-2-3-4-5; vertex 5 is a leaf
        int n = 5;
        int[][] edges = {{1,2},{2,3},{3,4},{4,5}};
        int[][] queries = {{5,0},{5,1},{5,100000}};
        long[] result = TreeQueries.treeQueries(n, edges, queries);
        assertArrayEquals(new long[]{0, 0, 0}, result);
    }

    // ── root query: no ancestors, result equals direct child count ────────────

    @Test void rootQueryKZero() {
        // Star: root 1 with leaves 2,3,4,5
        int n = 5;
        int[][] edges = {{1,2},{1,3},{1,4},{1,5}};
        int[][] queries = {{1,0}};
        // v=1 is the root; no deletions possible for root, c(1)=4
        long[] result = TreeQueries.treeQueries(n, edges, queries);
        assertEquals(4L, result[0]);
    }

    // ── single edge tree ──────────────────────────────────────────────────────

    @Test void twoNodeTree() {
        int n = 2;
        int[][] edges = {{1,2}};
        int[][] queries = {{2,0},{2,1},{1,0},{1,999}};
        long[] result = TreeQueries.treeQueries(n, edges, queries);
        // v=2: leaf, always 0; v=1: root with 1 child, no ancestors to delete → 1
        assertArrayEquals(new long[]{0, 0, 1, 1}, result);
    }

    // ── deep path: pulling ancestors is worth it only when k is small ─────────

    @Test void deepPathVaryingK() {
        // Path: 1-2-3-4-5  (each non-root node has 1 child except leaf)
        // Query v=5, k=0: delete 2,3,4 (3 deletions), c(5)=0 still (5 has no children)
        // Query v=3, k=0: delete 2 → c(3) gains children(2)-1 = 0 gained (2 had 1 child=3, so 0 new)
        // Actually v=3, k=0: ancestor=2 (d=1), gain=children(2)-1-1*0=0; ancestor=1 (d=2), gain=children(1)-1-2*0=0
        // Baseline c(3) = 1 (only child is 4). Best = 1.
        int n = 5;
        int[][] edges = {{1,2},{2,3},{3,4},{4,5}};
        int[][] queries = {{3,0},{3,1},{3,100}};
        long[] result = TreeQueries.treeQueries(n, edges, queries);
        // v=3 direct children = {4}, c=1. Ancestors: 2 (1 child=3, gain=0), 1 (1 child=2, gain=0)
        assertArrayEquals(new long[]{1, 1, 1}, result);
    }

    // ── wide tree: deleting parent of v brings many siblings ─────────────────

    @Test void wideParent() {
        // Tree: 1 is root with children {2,3,4,5,6}; vertex 2 has children {7,8,9}
        // Root (1) cannot be deleted, so siblings cannot be "pulled" under v=2.
        // c(2) starts at 3 and cannot increase here.
        int n = 9;
        int[][] edges = {{1,2},{1,3},{1,4},{1,5},{1,6},{2,7},{2,8},{2,9}};
        int[][] queries = {{2,0},{2,5}};
        long[] result = TreeQueries.treeQueries(n, edges, queries);
        assertArrayEquals(new long[]{3, 3}, result);
    }

    // ── performance: n=200000, q=200000 must finish in 2 seconds ─────────────

    @Test void performanceLargeChain() {
        assertTimeoutPreemptively(Duration.ofSeconds(2), () -> {
            int n = 200000;
            int[][] edges = new int[n - 1][2];
            for (int i = 2; i <= n; i++) edges[i - 2] = new int[]{i - 1, i};

            int[][] queries = new int[n][2];
            for (int i = 0; i < n; i++) queries[i] = new int[]{n, i};  // vary k

            long[] result = TreeQueries.treeQueries(n, edges, queries);
            assertNotNull(result);
            assertEquals(n, result.length);
        });
    }

    @Test void performanceLargeStarAllQueries() {
        assertTimeoutPreemptively(Duration.ofSeconds(2), () -> {
            int n = 200000;
            int[][] edges = new int[n - 1][2];
            for (int i = 2; i <= n; i++) edges[i - 2] = new int[]{1, i};

            int[][] queries = new int[n][2];
            for (int i = 0; i < n; i++) queries[i] = new int[]{i % (n - 1) + 2, i % 100};

            long[] result = TreeQueries.treeQueries(n, edges, queries);
            assertNotNull(result);
            assertEquals(n, result.length);
        });
    }
}
""",
    },
    {
        # ──────────────────────────────────────────────────────────────────────
        # Problem: 1600_E. Array Game (manual I/O conversion)
        # Source  : hard_problems_with_testsFromCodeForces.jsonl
        # ──────────────────────────────────────────────────────────────────────
        "id": "array_game_io",
        "title": "Deque Race: Increasing Sequence Duel",
        "class_name": "ArrayGameIO",

        "signature": "public static String solve(String input)",

        "description": """\
Versione leggermente riformulata:

Due giocatori (Alice e Bob) hanno un array di lunghezza `N`.
Costruiscono a turno una sequenza prendendo, a ogni mossa, un numero
solo da sinistra o da destra dell'array rimanente.

La sequenza costruita deve restare strettamente crescente.
Chi effettua l'ultima mossa valida vince.
Alice gioca per prima.

Dato l'input completo del problema, restituisci in output solo il nome
del vincitore (`Alice` oppure `Bob`) seguito da newline.

Implementa quindi un parser completo in `solve(String input)` e produci
esattamente il formato atteso.
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
        # Source  : hard_problems_with_testsFromCodeForces.jsonl
        # ──────────────────────────────────────────────────────────────────────
        "id": "replace_numbers_io",
        "title": "Bulk Value Substitution Stream",
        "class_name": "ReplaceNumbersIO",

        "signature": "public static String solve(String input)",

        "description": """\
Versione riformulata in modo leggero:

Gestisci una sequenza inizialmente vuota con due operazioni:
1) `1 x`: appendi `x` in coda.
2) `2 x y`: sostituisci tutte le occorrenze correnti di `x` con `y`.

Dopo tutte le query, stampa la sequenza finale.

Implementa parsing e output completi in `solve(String input)`.
Il formato di output deve essere identico a quello del problema originale.
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
Riformulazione leggera:

Data una griglia con muri `#`, celle libere `.`, e una posizione speciale `L`,
devi espandere le celle raggiungibili convertendo alcune `.` in `+` secondo
le regole del problema originale (versione Codeforces 1613E).

L'input può contenere più casi di test.
Restituisci la griglia trasformata per ogni caso, rispettando esattamente
il formato di output.
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
