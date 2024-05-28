
## String Splitting
### Mimic Regex
- Ex: Find all roots of 3(X-5)(X+6)(X-2)
	- Replace all brackets/invalid characters into 1 unused character (ie: turn left parenthesis and X into right parenthesis )
	- Then split string on that character
	- If `token[0]` is in '+-' then it is a valid root
	- To get unique roots, iterate sorted(set(roots))