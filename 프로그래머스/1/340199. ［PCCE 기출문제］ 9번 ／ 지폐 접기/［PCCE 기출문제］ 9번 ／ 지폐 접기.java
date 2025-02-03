class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;
        int minWallet = Integer.min(wallet[0], wallet[1]);
        int maxWallet = Integer.max(wallet[0], wallet[1]);

        while (true) {
            int minBill = Integer.min(bill[0], bill[1]);
            int maxBill = Integer.max(bill[0], bill[1]);

            if (minBill <= minWallet && maxBill <= maxWallet) {
                break;
            }

            if (bill[0] > bill[1]) {
                bill[0] /= 2;
            }
            else {
                bill[1] /= 2;
            }

            answer++;
        }

        return answer;
    }
}