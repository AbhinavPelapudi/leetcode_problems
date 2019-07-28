/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf); 
 */
/**
 * The read4 API is defined in the parent class Reader4.
 *     int read4(char[] buf); 
 */
public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Number of characters to read
     * @return    The number of actual characters read
     */
    private char[] buff = new char[4]; 
    private int curr = 0;
    private int count = 0;

    public int read(char[] buf, int n) {
        int read = n;
        while(read > 0){
            if(curr == count) {
                count = read4(buff);
                curr = 0;
            }
            if(count == 0) break; 
            buf[n-read--] = buff[curr++];
        }
        return n-read;
    }
}