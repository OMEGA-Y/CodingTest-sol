import java.io.*;
import java.util.Deque;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class deque_10866 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder builder = new StringBuilder();
		
		Deque<Integer> pq = new LinkedList<>();
		int n = Integer.parseInt(br.readLine());
		
		int token = 0;
		for(int i=0; i<n; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			switch(st.nextToken()) {
				case "push_front":
					token = Integer.parseInt(st.nextToken());
					pq.offerFirst(token);
					break;
				case "push_back":
					token = Integer.parseInt(st.nextToken());
					pq.offerLast(token);
					break;
				case "pop_front":
					builder.append(pq.isEmpty()?-1:pq.pollFirst()).append("\n");
					break;
				case "pop_back":
					builder.append(pq.isEmpty()?-1:pq.pollLast()).append("\n");
					break;
				case "size":
					builder.append(pq.size()).append("\n");
					break;
				case "empty":
					builder.append(pq.isEmpty()?1:0).append("\n");
					break;
				case "front":
					builder.append(pq.isEmpty()?-1:pq.peek()).append("\n");
					break;
				case "back":
					builder.append(pq.isEmpty()?-1:pq.peekLast()).append("\n");
					break;
			}
		}
		System.out.println(builder.toString());
	}
}
