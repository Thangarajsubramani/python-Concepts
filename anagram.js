// anagram

str1 = 'silent'
str2 = 'listen'
// sorting 
function anagram(str1, str2){
  let word1 = str1.toLowerCase().split('').sort().join('').trim()
  let word2 = str2.toLowerCase().split('').sort().join('').trim()
  console.log(word2);
  return word1 == word1 ? true: false
}

isAnagram = anagram(str1, str2);

console.log(isAnagram);

// using hash table array
function anagram(word1 , word2){
  counts = []
  let normalizedWord1 = word1.replace(/[^A-Za-z]+/g, '').toLowerCase();
  let normalizedWord2 = word2.replace(/[^A-Za-z]+/g, '').toLowerCase();
  // console.log(normalizedWord1);

  for(let i=0 ; i < normalizedWord1.length; i++){
    var index = normalizedWord1.charCodeAt(i)-97
    console.log(index);
    counts[index] = (counts[index] || 0) + 1;
  }

  for(let i=0; i < normalizedWord2.length; i++ ){
    var index = normalizedWord2.charCodeAt(i)-97

    if(!counts[index]) return false
    else{
      counts[index] == counts[index] -1
    }
    
  }

  return true
}

anagram('4si@lent', 'listen')


