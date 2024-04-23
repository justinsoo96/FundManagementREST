CREATE TABLE Fund (
    fund_id INT PRIMARY KEY AUTO_INCREMENT,
    fund_name VARCHAR(100) NOT NULL,
    fund_manager_name VARCHAR(100) NOT NULL,
    fund_description TEXT,
    fund_nav DECIMAL(20, 2) NOT NULL,
    fund_creation_date DATE NOT NULL,
    fund_performance DECIMAL(5, 2) NOT NULL
);

CREATE TABLE Investor (
    investor_id INT PRIMARY KEY AUTO_INCREMENT,
    investor_name VARCHAR(100) NOT NULL,
    -- Add other columns for investor information
);

CREATE TABLE FundInvestor (
    id INT PRIMARY KEY AUTO_INCREMENT,
    fund_id INT,
    investor_id INT,
    FOREIGN KEY (fund_id) REFERENCES Fund(fund_id),
    FOREIGN KEY (investor_id) REFERENCES Investor(investor_id)
);

-- In this modified schema:

-- 1. We have a new table named Investor to store information about each investor.
-- 2. Each investor is identified by a unique investor_id.
-- 3. We have an intermediary table named FundInvestor to establish a many-to-many relationship between funds and investors.
-- 4. This table contains foreign keys fund_id and investor_id referencing the fund_id and investor_id columns in the Fund and Investor tables, respectively.