# collatz-cycle-visualization
**Uses numpy and matplotlib for visualization of collatz cycle**

The aim of this project is to enable visualizations of any cycle similar to collatz to maybe establish a new perspective on the original collatz sequence.

**Input: rules for_even_ & _odd_ and _minimum_ & _lower_ bound.**          
*( make sure that the sequence does not go to infinity )


## Example graphs for difference rules
### Rule1: Original 3n+1
<img src="/graphs/rule_1_iterations.png" width="400"/> <img src="/graphs/rule_1_max.png" width="400"/> 

### Rule 2: 3n+1 extended to negative numbers
<img src="/graphs/rule_1_iterations_neg.png" width="400"/> <img src="/graphs/rule_1_max_neg.png" width="400"/> 


### Rule 3: Even: 3n+1, odd: (0.5*n)+0.5
<img src="/graphs/rule_3_iterations.png" width="400"/> <img src="/graphs/rule_3_max.png" width="400"/> 

### Rule 4: Even: 2n+1, odd: (0.5*n)+0.5
<img src="/graphs/rule_4_iterations.png" width="400"/> <img src="/graphs/rule_4_max.png" width="400"/> 

### Rule 5: Even: -n/2 odd: -3*n+1
<img src="/graphs/rule_5_iterations.png" width="400"/> <img src="/graphs/rule_5_max.png" width="400"/> 

#### Further improvements to make
* Add a way of detecting when a number approaches infinity
* ~~Extend program to negative numbers
* Make an algorithm to find many collatz like sequences





