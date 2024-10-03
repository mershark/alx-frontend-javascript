function pascalTriangle(n) {
    if (n <= 0) return [];

    const triangle = [[1]];

    for (let i = 1; i < n; i++) {
        const row = [1];

        for (let j = 1; j < i; j++) {
            row.push(triangle[i - 1][j - 1] + triangle[i - 1][j]);
        }

        row.push(1);
        triangle.push(row);
    }

    return triangle;
}

function printTriangle(triangle) {
    triangle.forEach(row => {
        console.log(`[${row.join(',')}]`);
    });
}

printTriangle(pascalTriangle(5));
