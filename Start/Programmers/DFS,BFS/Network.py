#네트워크

#자바
"""
class Solution {
    
    private int count;

	public int solution(int n, int[][] computers) {

		boolean[] visit = new boolean[n];

		// 전체 컴퓨터 방문
		for (int i = 0; i < n; i++) {

			// 이미 방문 도장이 찍혀있으면 가지 않음 
			if (!visit[i]) {
				
				// 첫 노드부터 재귀함수 시작
				dfs(n, i, computers, visit);
				count++;
			}
		}

		return count;
	}

	private void dfs(int n, int index, int[][] computers, boolean[] visit) {

		// 방문확인
		visit[index] = true;

		// 노드 방문
		for (int i = 0; i < n; i++) {

			// 연결된 노드, 자신 제외, 아직 방문기록이 없는 노드
			if (computers[index][i] == 1 && i != index && !visit[i]) {
				dfs(n, i, computers, visit);
			}
		}
	}
}
"""
#이미 방문했는지 확인하는 작업 중요
#파이썬 DFS
def dfs(graph, v, visited):
    visited[v] = True
    n = len(graph)
    
    for node in range(n):
        if graph[v][node] == 1 and visited[node] == False:
            dfs(graph, node, visited)
            
def solution(n, computers):
    answer = 0
    visited = [0]*n
    
    for start in range(n): # n개의 node를 각각 시작 노드로 dfs
        if visited[start] == 0: # 이전 탐색에서 방문하지 않았을 경우에만 탐색 시작
            dfs(computers, start, visited)
            answer += 1
    
    return answer