function linearSearch(haystack: number[], needle: number): number {
    for (let i = 0; i < haystack.length; i++) {
        if (haystack[i] === needle) {
            return i;
        }
    }
    return -1;
}

function test() {
    process.stdin.resume();
    process.stdin.setEncoding('utf-8');
    process.stdin.on('data', (input: string) => {
        let lines = input.split('\n');
        let linesSplit = lines.map((line) => line.split(' '));
        let numbers = linesSplit[1].map((x) => parseInt(x));
        let queries = linesSplit[2].map((x) => parseInt(x));
        let answers: number[] = [];
        for (let query of queries) {
            answers.push(linearSearch(numbers, query));
        }
        console.log(answers.join(' '));
    });
}

(function() {
    test();
})();
