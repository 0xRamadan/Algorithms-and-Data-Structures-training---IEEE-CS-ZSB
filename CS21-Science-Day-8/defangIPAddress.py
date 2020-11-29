# name: mahmoud Abdallah
# mail: mahmoud.abdallah@ieee-zsb.org
# link to the problem: https://leetcode.com/problems/defanging-an-ip-address/submissions/
# time complexity: O(n) or I can say O(1) because IP addresses are limited to certain numbers.
# in the same way I can say that Space complexity is O(1)

class Solution:
    def defangIPaddr(self, address: str) -> str:
        self.__init__ = self
        self.address = address
        address = address.replace(".", "[.]")
        return address