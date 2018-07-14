// ===============================================
// Assume that rand() is O(1) time, O(1) space function.
// What is the time, space complexity of following code :
int a = 0, b = 0;    
for (i = 0; i < N; i++) {
    a = a + rand();  
}
for (j = 0; j < M; j++) {
    b = b + rand();
} 

 // O(N + M) time, O(1) space


// ===============================================
// What is the time complexity of the following code :
int a = 0, i = N;
while (i > 0) {
    a += i;
    i /= 2;
}

// O(log N)


// ===============================================
// In a competition, four different functions are observed. All the functions use a single for loop and within the for loop, same set of statements are executed.
// Consider the following for loops:
A) for(i = 0; i < n; i++)
 
B) for(i = 0; i < n; i += 2)

C) for(i = 1; i < n; i *= 2)

D) for(i = n; i > -1; i /= 2)

// If n is the size of input(positive), which function is the most efficient? In other words, which loop completes the fastest.

// C


// ===============================================
// What is the worst case time complexity of the following code :
/* 
 * V is sorted 
 * V.size() = N
 * The function is initially called as searchNumOccurrence(V, k, 0, N-1)
 */
int searchNumOccurrence(vector<int> &V, int k, int start, int end) {
    if (start > end) return 0;
    int mid = (start + end) / 2;
    if (V[mid] < k) return searchNumOccurrence(V, k, mid + 1, end);
    if (V[mid] > k) return searchNumOccurrence(V, k, start, mid - 1);
    return searchNumOccurrence(V, k, start, mid - 1) + 1 + searchNumOccurrence(V, k, mid + 1, end);
}


// O(N)


// ===============================================
// What is the time complexity of the following code :
int j = 0;
for(int i = 0; i < n; ++i) {
    while(j < n && arr[i] < arr[j]) {
        j++;
    }
}

// O(n)


// ===============================================