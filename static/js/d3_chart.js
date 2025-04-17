fetch("/api/progress")
    .then(res => res.json())
    .then(data => {
        const dataset = data.data;
        if (!dataset.length) return;

        const margin = {top: 20, right: 30, bottom: 40, left: 50};
        const width = 500 - margin.left - margin.right;
        const height = 300 - margin.top - margin.bottom;

        const svg = d3.select("#progressChart")
            .append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
            .append("g")
            .attr("transform", `translate(${margin.left},${margin.top})`);

        const x = d3.scaleLinear()
            .domain([0, dataset.length - 1])
            .range([0, width]);

        const y = d3.scaleLinear()
            .domain([d3.min(dataset, d => d.current_weight) - 5, d3.max(dataset, d => d.current_weight) + 5])
            .range([height, 0]);

        svg.append("g")
            .attr("transform", `translate(0,${height})`)
            .call(d3.axisBottom(x).ticks(dataset.length));

        svg.append("g")
            .call(d3.axisLeft(y));

        svg.append("path")
            .datum(dataset)
            .attr("fill", "none")
            .attr("stroke", "steelblue")
            .attr("stroke-width", 2)
            .attr("d", d3.line()
                .x((d, i) => x(i))
                .y(d => y(d.current_weight))
            );

        svg.selectAll("dot")
            .data(dataset)
            .enter().append("circle")
            .attr("cx", (d, i) => x(i))
            .attr("cy", d => y(d.current_weight))
            .attr("r", 4)
            .attr("fill", "red");
    });
