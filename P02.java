Title: Implement A star Algorithm for any game search problem.

import java.util.*;

class Node {
    int id, h;
    List<Edge> n;

    Node(int i, int h) {
        id = i;
        this.h = h;
        n = new ArrayList<>();
    }
}

class Edge {
    Node t;
    int c;

    Edge(Node t, int c) {
        this.t = t;
        this.c = c;
    }
}

public class AStar {
    public static int[] astar(Node s, Node g) {
        PriorityQueue<Node> o = new PriorityQueue<>((a, b) -> a.h - b.h);
        Map<Node, Integer> gMap = new HashMap<>();
        Map<Node, Node> cF = new HashMap<>();

        o.add(s);
        gMap.put(s, 0);

        while (!o.isEmpty()) {
            Node c = o.poll();

            if (c == g) return reconstructPath(cF, c);

            for (Edge e : c.n) {
                Node n = e.t;
                int tg = gMap.getOrDefault(c, Integer.MAX_VALUE) + e.c;

                if (tg < gMap.getOrDefault(n, Integer.MAX_VALUE)) {
                    cF.put(n, c);
                    gMap.put(n, tg);
                    o.add(n);
                }
            }
        }

        return new int[0];
    }

    private static int[] reconstructPath(Map<Node, Node> cF, Node c) {
        List<Integer> p = new ArrayList<>();
        p.add(c.id);

        while (cF.containsKey(c)) {
            c = cF.get(c);
            p.add(c.id);
        }

        Collections.reverse(p);
        return p.stream().mapToInt(Integer::intValue).toArray();
    }

    public static void main(String[] args) {
        Node a = new Node(0, 10);
        Node b = new Node(1, 8);
        Node c = new Node(2, 5);
        Node d = new Node(3, 2);
        Node e = new Node(4, 0);

        a.n.add(new Edge(b, 5));
        a.n.add(new Edge(c, 3));
        b.n.add(new Edge(d, 2));
        c.n.add(new Edge(d, 2));
        c.n.add(new Edge(e, 4));
        d.n.add(new Edge(e, 3));

        int[] p = astar(a, e);
        System.out.println("Shortest Path: " + Arrays.toString(p)); // Output: Shortest Path: [0, 2, 4]
    }
}

Output -:

Shortest Path: [0, 2, 4]
=== Code Execution Successful ===
