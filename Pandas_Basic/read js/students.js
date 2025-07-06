const students = [
  {
    "student_id":1,
    "name":"Student 1",
    "age":19,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":2.54
  },
  {
    "student_id":2,
    "name":"Student 2",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":3.93
  },
  {
    "student_id":3,
    "name":"Student 3",
    "age":19,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.91
  },
  {
    "student_id":4,
    "name":"Student 4",
    "age":21,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":3.68
  },
  {
    "student_id":5,
    "name":"Student 5",
    "age":21,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":1,
    "gpa":2.39
  },
  {
    "student_id":6,
    "name":"Student 6",
    "age":24,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":3,
    "gpa":2.82
  },
  {
    "student_id":7,
    "name":"Student 7",
    "age":21,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.4
  },
  {
    "student_id":8,
    "name":"Student 8",
    "age":24,
    "gender":"F",
    "enrollment_year":2023,
    "department_id":1,
    "gpa":2.28
  },
  {
    "student_id":9,
    "name":"Student 9",
    "age":21,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":1,
    "gpa":2.27
  },
  {
    "student_id":10,
    "name":"Student 10",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.94
  },
  {
    "student_id":11,
    "name":"Student 11",
    "age":24,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.43
  },
  {
    "student_id":12,
    "name":"Student 12",
    "age":20,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":1,
    "gpa":2.08
  },
  {
    "student_id":13,
    "name":"Student 13",
    "age":23,
    "gender":"M",
    "enrollment_year":2023,
    "department_id":1,
    "gpa":2.8
  },
  {
    "student_id":14,
    "name":"Student 14",
    "age":18,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.87
  },
  {
    "student_id":15,
    "name":"Student 15",
    "age":21,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":1,
    "gpa":3.49
  },
  {
    "student_id":16,
    "name":"Student 16",
    "age":19,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.5
  },
  {
    "student_id":17,
    "name":"Student 17",
    "age":21,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.37
  },
  {
    "student_id":18,
    "name":"Student 18",
    "age":19,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":2.16
  },
  {
    "student_id":19,
    "name":"Student 19",
    "age":23,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":2.86
  },
  {
    "student_id":20,
    "name":"Student 20",
    "age":23,
    "gender":"F",
    "enrollment_year":2023,
    "department_id":1,
    "gpa":3.38
  },
  {
    "student_id":21,
    "name":"Student 21",
    "age":23,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":2.12
  },
  {
    "student_id":22,
    "name":"Student 22",
    "age":19,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":1,
    "gpa":3.83
  },
  {
    "student_id":23,
    "name":"Student 23",
    "age":21,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.88
  },
  {
    "student_id":24,
    "name":"Student 24",
    "age":23,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.48
  },
  {
    "student_id":25,
    "name":"Student 25",
    "age":22,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":1,
    "gpa":2.19
  },
  {
    "student_id":26,
    "name":"Student 26",
    "age":24,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":3,
    "gpa":2.37
  },
  {
    "student_id":27,
    "name":"Student 27",
    "age":19,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.87
  },
  {
    "student_id":28,
    "name":"Student 28",
    "age":19,
    "gender":"M",
    "enrollment_year":2023,
    "department_id":1,
    "gpa":3.28
  },
  {
    "student_id":29,
    "name":"Student 29",
    "age":21,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.03
  },
  {
    "student_id":30,
    "name":"Student 30",
    "age":19,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.31
  },
  {
    "student_id":31,
    "name":"Student 31",
    "age":19,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":2.87
  },
  {
    "student_id":32,
    "name":"Student 32",
    "age":23,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.46
  },
  {
    "student_id":33,
    "name":"Student 33",
    "age":21,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":2.1
  },
  {
    "student_id":34,
    "name":"Student 34",
    "age":23,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.13
  },
  {
    "student_id":35,
    "name":"Student 35",
    "age":24,
    "gender":"F",
    "enrollment_year":2020,
    "department_id":2,
    "gpa":2.32
  },
  {
    "student_id":36,
    "name":"Student 36",
    "age":24,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.24
  },
  {
    "student_id":37,
    "name":"Student 37",
    "age":23,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":2.68
  },
  {
    "student_id":38,
    "name":"Student 38",
    "age":24,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":3,
    "gpa":2.18
  },
  {
    "student_id":39,
    "name":"Student 39",
    "age":21,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.19
  },
  {
    "student_id":40,
    "name":"Student 40",
    "age":18,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.62
  },
  {
    "student_id":41,
    "name":"Student 41",
    "age":23,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.96
  },
  {
    "student_id":42,
    "name":"Student 42",
    "age":22,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":2,
    "gpa":2.35
  },
  {
    "student_id":43,
    "name":"Student 43",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.03
  },
  {
    "student_id":44,
    "name":"Student 44",
    "age":19,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":3.53
  },
  {
    "student_id":45,
    "name":"Student 45",
    "age":24,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":3.61
  },
  {
    "student_id":46,
    "name":"Student 46",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":2.69
  },
  {
    "student_id":47,
    "name":"Student 47",
    "age":19,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.93
  },
  {
    "student_id":48,
    "name":"Student 48",
    "age":18,
    "gender":"F",
    "enrollment_year":2020,
    "department_id":3,
    "gpa":3.3
  },
  {
    "student_id":49,
    "name":"Student 49",
    "age":21,
    "gender":"F",
    "enrollment_year":2020,
    "department_id":3,
    "gpa":2.1
  },
  {
    "student_id":50,
    "name":"Student 50",
    "age":21,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":3.9
  },
  {
    "student_id":51,
    "name":"Student 51",
    "age":21,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":3.77
  },
  {
    "student_id":52,
    "name":"Student 52",
    "age":22,
    "gender":"F",
    "enrollment_year":2020,
    "department_id":2,
    "gpa":2.52
  },
  {
    "student_id":53,
    "name":"Student 53",
    "age":18,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":1,
    "gpa":2.03
  },
  {
    "student_id":54,
    "name":"Student 54",
    "age":22,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.87
  },
  {
    "student_id":55,
    "name":"Student 55",
    "age":24,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.0
  },
  {
    "student_id":56,
    "name":"Student 56",
    "age":22,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.08
  },
  {
    "student_id":57,
    "name":"Student 57",
    "age":18,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":2,
    "gpa":3.37
  },
  {
    "student_id":58,
    "name":"Student 58",
    "age":18,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.23
  },
  {
    "student_id":59,
    "name":"Student 59",
    "age":24,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.89
  },
  {
    "student_id":60,
    "name":"Student 60",
    "age":18,
    "gender":"M",
    "enrollment_year":2023,
    "department_id":2,
    "gpa":3.89
  },
  {
    "student_id":61,
    "name":"Student 61",
    "age":18,
    "gender":"M",
    "enrollment_year":2023,
    "department_id":3,
    "gpa":3.73
  },
  {
    "student_id":62,
    "name":"Student 62",
    "age":21,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":3.27
  },
  {
    "student_id":63,
    "name":"Student 63",
    "age":24,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.6
  },
  {
    "student_id":64,
    "name":"Student 64",
    "age":20,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":3.35
  },
  {
    "student_id":65,
    "name":"Student 65",
    "age":20,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":3.15
  },
  {
    "student_id":66,
    "name":"Student 66",
    "age":18,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.26
  },
  {
    "student_id":67,
    "name":"Student 67",
    "age":20,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":3.62
  },
  {
    "student_id":68,
    "name":"Student 68",
    "age":20,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":3,
    "gpa":3.64
  },
  {
    "student_id":69,
    "name":"Student 69",
    "age":18,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":1,
    "gpa":3.25
  },
  {
    "student_id":70,
    "name":"Student 70",
    "age":20,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":1,
    "gpa":3.64
  },
  {
    "student_id":71,
    "name":"Student 71",
    "age":22,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":3.3
  },
  {
    "student_id":72,
    "name":"Student 72",
    "age":19,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.41
  },
  {
    "student_id":73,
    "name":"Student 73",
    "age":24,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.55
  },
  {
    "student_id":74,
    "name":"Student 74",
    "age":19,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":3,
    "gpa":2.43
  },
  {
    "student_id":75,
    "name":"Student 75",
    "age":18,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":2.75
  },
  {
    "student_id":76,
    "name":"Student 76",
    "age":21,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":2.08
  },
  {
    "student_id":77,
    "name":"Student 77",
    "age":24,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":3.24
  },
  {
    "student_id":78,
    "name":"Student 78",
    "age":18,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.67
  },
  {
    "student_id":79,
    "name":"Student 79",
    "age":21,
    "gender":"F",
    "enrollment_year":2023,
    "department_id":3,
    "gpa":3.31
  },
  {
    "student_id":80,
    "name":"Student 80",
    "age":19,
    "gender":"F",
    "enrollment_year":2020,
    "department_id":3,
    "gpa":2.77
  },
  {
    "student_id":81,
    "name":"Student 81",
    "age":18,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":2,
    "gpa":3.36
  },
  {
    "student_id":82,
    "name":"Student 82",
    "age":24,
    "gender":"M",
    "enrollment_year":2020,
    "department_id":3,
    "gpa":2.68
  },
  {
    "student_id":83,
    "name":"Student 83",
    "age":24,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.52
  },
  {
    "student_id":84,
    "name":"Student 84",
    "age":23,
    "gender":"F",
    "enrollment_year":2023,
    "department_id":2,
    "gpa":2.99
  },
  {
    "student_id":85,
    "name":"Student 85",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":3,
    "gpa":3.39
  },
  {
    "student_id":86,
    "name":"Student 86",
    "age":20,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.7
  },
  {
    "student_id":87,
    "name":"Student 87",
    "age":21,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":1,
    "gpa":3.87
  },
  {
    "student_id":88,
    "name":"Student 88",
    "age":23,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":2.08
  },
  {
    "student_id":89,
    "name":"Student 89",
    "age":20,
    "gender":"M",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":2.84
  },
  {
    "student_id":90,
    "name":"Student 90",
    "age":20,
    "gender":"F",
    "enrollment_year":2023,
    "department_id":2,
    "gpa":3.94
  },
  {
    "student_id":91,
    "name":"Student 91",
    "age":18,
    "gender":"M",
    "enrollment_year":2022,
    "department_id":2,
    "gpa":3.1
  },
  {
    "student_id":92,
    "name":"Student 92",
    "age":20,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":2.85
  },
  {
    "student_id":93,
    "name":"Student 93",
    "age":22,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":3.14
  },
  {
    "student_id":94,
    "name":"Student 94",
    "age":24,
    "gender":"F",
    "enrollment_year":2019,
    "department_id":2,
    "gpa":3.15
  },
  {
    "student_id":95,
    "name":"Student 95",
    "age":23,
    "gender":"F",
    "enrollment_year":2022,
    "department_id":3,
    "gpa":3.46
  },
  {
    "student_id":96,
    "name":"Student 96",
    "age":20,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":2,
    "gpa":2.26
  },
  {
    "student_id":97,
    "name":"Student 97",
    "age":18,
    "gender":"F",
    "enrollment_year":2021,
    "department_id":3,
    "gpa":2.5
  },
  {
    "student_id":98,
    "name":"Student 98",
    "age":22,
    "gender":"M",
    "enrollment_year":2023,
    "department_id":1,
    "gpa":3.16
  },
  {
    "student_id":99,
    "name":"Student 99",
    "age":19,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":3.73
  },
  {
    "student_id":100,
    "name":"Student 100",
    "age":24,
    "gender":"M",
    "enrollment_year":2021,
    "department_id":1,
    "gpa":3.12
  }
];

export default students;
