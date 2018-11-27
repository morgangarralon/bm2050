-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2018-11-27 18:02:06.198

-- tables
-- Table: Account
CREATE TABLE Account (
    Id integer NOT NULL CONSTRAINT Account_pk PRIMARY KEY,
    IsAdmin boolean NOT NULL,
    FirstName varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    EmailAddress integer NOT NULL,
    RoleId integer NOT NULL,
    CreationDate datetime NOT NULL,
    LastLogin datetime NOT NULL,
    Username varchar(255) NOT NULL,
    Password varchar(255) NOT NULL,
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
    Answer varchar(1000) NOT NULL,
    AnswerId integer,
    TimeStamp datetime NOT NULL,
    PollOpionid integer,
    Score integer NOT NULL,
    CONSTRAINT Answer_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id),
    CONSTRAINT Answer_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id),
    CONSTRAINT Answer_Answer FOREIGN KEY (AnswerId)
    REFERENCES Answer (Id),
    CONSTRAINT Answer_PollOpions FOREIGN KEY (PollOpionid)
    REFERENCES PollOpion (id)
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
    Name integer NOT NULL
);

-- Table: DomainExpertise
CREATE TABLE DomainExpertise (
    Id integer NOT NULL CONSTRAINT DomainExpertise_pk PRIMARY KEY,
    Name varchar(255) NOT NULL
);

-- Table: PollOpion
CREATE TABLE PollOpion (
    id integer NOT NULL CONSTRAINT PollOpion_pk PRIMARY KEY,
    OptionName varchar(255) NOT NULL,
    QuestionId integer NOT NULL,
    CONSTRAINT PollOpions_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id)
);

-- Table: Question
CREATE TABLE Question (
    Id integer NOT NULL CONSTRAINT Question_pk PRIMARY KEY,
    Question varchar(1000) NOT NULL,
    TimeStamp datetime NOT NULL,
    AnswerStatusId integer NOT NULL,
    IsPoll boolean NOT NULL,
    AccountId integer NOT NULL,
    Score integer NOT NULL,
    CONSTRAINT Question_AnswerStatus FOREIGN KEY (AnswerStatusId)
    REFERENCES AnswerStatus (Id),
    CONSTRAINT Question_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id)
);

-- Table: QuestionDomainExpertise
CREATE TABLE QuestionDomainExpertise (
    DomainExpertiseId integer NOT NULL,
    QuestionId integer NOT NULL,
    CONSTRAINT QuestionDomainExpertise_pk PRIMARY KEY (DomainExpertiseId,QuestionId),
    CONSTRAINT QuestionDomainExpertise_DomainExpertise FOREIGN KEY (DomainExpertiseId)
    REFERENCES DomainExpertise (Id),
    CONSTRAINT QuestionDomainExpertise_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id)
);

-- Table: Role
CREATE TABLE Role (
    Id integer NOT NULL CONSTRAINT Role_pk PRIMARY KEY,
    Name integer NOT NULL
);

-- Table: Vote
CREATE TABLE Vote (
    Id integer NOT NULL CONSTRAINT Vote_pk PRIMARY KEY,
    AccountId integer NOT NULL,
    AnswerId integer NOT NULL,
    QuestionId integer NOT NULL,
    TimeStamp datetime NOT NULL,
    IsUpvote boolean NOT NULL,
    CONSTRAINT Vote_Account FOREIGN KEY (AccountId)
    REFERENCES Account (Id),
    CONSTRAINT Vote_Answer FOREIGN KEY (AnswerId)
    REFERENCES Answer (Id),
    CONSTRAINT Vote_Question FOREIGN KEY (QuestionId)
    REFERENCES Question (Id)
);

-- End of file.
