package com.vrazhenko.documentfeature;

import jakarta.persistence.*;

@Entity
@Table(name = "counterparties")
public class Counterparty {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false)
    private String name;

    @Column(name = "inn")
    private String inn;

    @Column(name = "address")
    private String address;

    public Counterparty() {}

    public Counterparty(String name, String inn, String address) {
        this.name = name;
        this.inn = inn;
        this.address = address;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }

    public String getName() { return name; }
    public void setName(String name) { this.name = name; }

    public String getInn() { return inn; }
    public void setInn(String inn) { this.inn = inn; }

    public String getAddress() { return address; }
    public void setAddress(String address) { this.address = address; }
}
