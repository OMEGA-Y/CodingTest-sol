import java.io.*;
import java.util.*;

public class queue_10845 {
	
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));


		br.readLine(); // int n = Integer.parseInt(br.readLine());
		List<Integer> q = new LinkedList<>();
		
		String input = "";
		while((input=br.readLine()) != null) {
			String[] token = input.split(" ");
			if(token[0].equals("push")){
				q.add(Integer.parseInt(token[1]));
			}
			else if(token[0].equals("size")) {
				bw.write(Integer.toString(q.size())+"\n");
			}
			else if(token[0].equals("pop")) {
				if(q.isEmpty()) {
					bw.write("-1\n"); // bw는 내용물을 string으로 바꿔서 출력해야함
				}else {
					int tmp = q.remove(0);
					bw.write(Integer.toString(tmp)+"\n");
				}
			}
			else if(token[0].equals("empty")) {
				bw.write(q.isEmpty()?"1\n":"0\n"); // if-else 문을 깔끔하게 줄임
			}
			else if(token[0].equals("front")) {
				bw.write(q.isEmpty()?"-1":Integer.toString(q.get(0)));
				bw.newLine(); // bw는 줄바꿈을 하려면 내용물에 \n을 추가하거나 br.newLine()을 추가해야함
			}
			else {
				bw.write(q.isEmpty()?"-1":Integer.toString(q.get(q.size()-1)));
				bw.newLine();
			}
		}
		
		bw.flush();
		bw.close();
		br.close();
	}
}
