// 第一題
//O(n)
function calculate(min, max, step) {
  var sum = 0;
  for (var i = min; i < max + 1; i = i + step) {
    sum = sum + i;
  }
  console.log(sum);
}
calculate(1, 3, 1);
calculate(4, 8, 2);
calculate(-1, 2, 2);

//第二題
//O(n)
function avg(data) {
  sum = 0;
  nonmanagerNum = 0;
  data["employees"].forEach((element) => {
    if (!element["manager"]) {
      sum += element["salary"];
      nonmanagerNum += 1;
    }
  });
  console.log(sum / nonmanagerNum);
}

avg({
  employees: [
    {
      name: "John",
      salary: 30000,
      manager: false,
    },
    {
      name: "Bob",
      salary: 60000,
      manager: true,
    },
    {
      name: "Jenny",
      salary: 50000,
      manager: false,
    },
    {
      name: "Tony",
      salary: 40000,
      manager: false,
    },
  ],
});

// 第三題
//O(1)
function func(a) {
  return operator;
  function operator(b, c) {
    console.log(b * c + a);
  }
}
func(2)(3, 4);
func(5)(1, -5);
func(-3)(2, 9);

//第四題 用quicksort 由大到小排序，比前兩個數字相乘或最後兩個負數相乘
//O(nlogn)
function maxProduct(nums) {
  function swap(nums, leftIndex, rightIndex) {
    var temp = nums[leftIndex];
    nums[leftIndex] = nums[rightIndex];
    nums[rightIndex] = temp;
  }

  function partition(nums, left, right) {
    var pivot = nums[left];
    var i = left + 1;
    var j = right;
    var done = false;
    if (left < right) {
      while (done === false) {
        while (i <= j && nums[i] > pivot) {
          i++;
        }

        while (i <= j && nums[j] < pivot) {
          j--;
        }

        if (j < i) {
          done = true;
          
        } else {
          // swap(nums, i, j);
          [nums[i], nums[j]] = [nums[j], nums[i]];
        }
      }
      // swap(nums, left, j)
      [nums[left], nums[j]] = [nums[j], nums[left]];
      return j;
    }
  }

  function quickSort(nums, left, right) {
    var index;
    if (left < right) {
      index = partition(nums, left, right);
      quickSort(nums, left, index - 1);
      quickSort(nums, index + 1, right);
    }
    return nums;
  }
  var sortedArray = quickSort(nums, 0, nums.length - 1);
  if (
    sortedArray[0] * sortedArray[1] >
    sortedArray[sortedArray.length - 1] * sortedArray[sortedArray.length - 2]
  ) {
    console.log(sortedArray[0] * sortedArray[1]);
  } else {
    console.log(
      sortedArray[sortedArray.length - 1] * sortedArray[sortedArray.length - 2]
    );
  }
}

maxProduct([5, 20, 2, 6]);
maxProduct([10, -20, 0, 3]);
maxProduct([10, -20, 0, -3]);
maxProduct([-1, 2])
maxProduct([-1, 0, 2]);
maxProduct([5, -1, -2, 0]);
maxProduct([-5, -2]);

//第五題
//O(n^2)
function twoSum(nums, target) {
  // your code here
  for (var i = 0; i < nums.length; i++) {
    if (nums.find((x) => x == target - nums[i])) {
      return [i, nums.findIndex((x) => x == target - nums[i])];
    } else {
      return -1;
    }
  }
}
let result = twoSum([2, 11, 7, 15], 9);
console.log(result);

//第六題
//O(n)
function maxZeros(nums) {
  var numString = "";
  for (var i = 0; i < nums.length; i++) {
    numString += nums[i];
  }
  arratString = numString.split(1);
  maxLength = 0;
  for (var i = 0; i < arratString.length; i++) {
    if (arratString[i].length > maxLength) {
      maxLength = arratString[i].length;
    }
  }
  console.log(maxLength);
}
maxZeros([0, 1, 0, 0]);
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]);
maxZeros([1, 1, 1, 1, 1]);
maxZeros([0, 0, 0, 1, 1]);
