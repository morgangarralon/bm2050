-- Created by Erik Stevens
-- Last modification date: 2018-11-26 15:54:51.9

-- tables
-- Table: Account
CREATE TABLE Account (
    Id integer NOT NULL CONSTRAINT Account_pk PRIMARY KEY,
    IsAdmin boolean,
    FirstName integer,
    LastName integer,
    EmailAddress integer,
    RoleId integer NOT NULL,
    CONSTRAINT Account_Roles FOREIGN KEY (RoleId)
    REFERENCES Role (Id)
);

-- Table: AccountDomainExpertise
CREATE TABLE AccountDomainExpertise (
    AccountId integer NOT NULL,
    DomainExpertiseId integer NOT NULL,
    CONSTRAINT AccountDomainExpertise_pk PRIMARY KEY (AccountId,DomainExpertiseId),
    CONSTRAINT AccountDomainExpertise_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id),
    CONSTRAINT AccountDomainExpertise_DomainExpertise FOREIGN KEY (DomainExpertiseId)
    REFERENCES DomainExpertise (Id)
);

-- Table: Answer
CREATE TABLE Answer (
    Id integer NOT NULL CONSTRAINT Answer_pk PRIMARY KEY,
    QuestionId integer NOT NULL,
    AccountId integer NOT NULL,
    Answer varchar(1000),
    AnswerId integer,
    CONSTRAINT Answer_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id),
    CONSTRAINT Answer_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id),
    CONSTRAINT Answer_Answer FOREIGN KEY (AnswerId)
    REFERENCES Answer (Id)
);

-- Table: AnswerDomainExpertise
CREATE TABLE AnswerDomainExpertise (
    AnswerId integer NOT NULL,
    DomainExpertiseId integer NOT NULL,
    CONSTRAINT AnswerDomainExpertise_pk PRIMARY KEY (AnswerId,DomainExpertiseId),
    CONSTRAINT AnswerDomainExpertise_Answer FOREIGN KEY (AnswerId)
    REFERENCES Answer (Id),
    CONSTRAINT AnswerDomainExpertise_DomainExpertise FOREIGN KEY (DomainExpertiseId)
    REFERENCES DomainExpertise (Id)
);

-- Table: AnswerStatus
CREATE TABLE AnswerStatus (
    Id integer NOT NULL CONSTRAINT AnswerStatus_pk PRIMARY KEY,
    Name integer
);

-- Table: DomainExpertise
CREATE TABLE DomainExpertise (
    Id integer NOT NULL CONSTRAINT DomainExpertise_pk PRIMARY KEY,
    Name varchar(255)
);

-- Table: Question
CREATE TABLE Question (
    Id integer NOT NULL CONSTRAINT Question_pk PRIMARY KEY,
    Question varchar(1000),
    TimeStamp datetime,
    AnswerStatusId integer NOT NULL,
    IsPoll boolean,
    CONSTRAINT Question_AnswerStatus FOREIGN KEY (AnswerStatusId)
    REFERENCES AnswerStatus (Id)
);

-- Table: Role
CREATE TABLE Role (
    Id integer NOT NULL CONSTRAINT Role_pk PRIMARY KEY,
    Name integer
);

-- Table: Vote
CREATE TABLE Vote (
    Id integer NOT NULL CONSTRAINT Vote_pk PRIMARY KEY,
    AccountId integer NOT NULL,
    AnswerId integer NOT NULL,
    QuestionId integer NOT NULL,
    CONSTRAINT Vote_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id),
    CONSTRAINT Vote_Answer FOREIGN KEY (AnswerId)
    REFERENCES Answer (Id),
    CONSTRAINT Vote_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id)
);

-- End of file.

