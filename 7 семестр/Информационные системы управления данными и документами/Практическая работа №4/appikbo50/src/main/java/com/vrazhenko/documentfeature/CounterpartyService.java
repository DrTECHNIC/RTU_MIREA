package com.vrazhenko.documentfeature;

import org.springframework.stereotype.Service;
import java.util.List;

@Service
public class CounterpartyService {

    private final CounterpartyRepository counterpartyRepository;

    public CounterpartyService(CounterpartyRepository counterpartyRepository) {
        this.counterpartyRepository = counterpartyRepository;
    }

    public List<Counterparty> findAll() {
        return counterpartyRepository.findAll();
    }

    public Counterparty save(Counterparty counterparty) {
        return counterpartyRepository.save(counterparty);
    }
}
