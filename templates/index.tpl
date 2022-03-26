<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Registos de Exames Médicos Desportivos</title>
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>Registos de Exames Médicos Desportivos</h1>

        <h2>Indicadores estatísticos</h2>

        <ul>
            <li>{{link(Age Gender distribution, age_gender_distrib.tpl)}}</li>
            {{stats(age_gender_distrib)}}
            <li>{{link(Federated by year , federated_by_year.tpl)}}</li>
            {{stats(federated_by_year)}}
            <li>{{link(Gender by year,gender_by_year.tpl)}}</li>
            {{stats(gender_by_year)}}
            <li>{{link(Location Distribution,location_distrib.tpl)}}</li>
            {{stats(location_distrib)}}
            <li>{{link(Results by year, result_by_year.tpl)}}</li>
            {{stats(result_by_year)}}
            <li>{{link(Sport by year, sport_by_year.tpl)}}</li>
            {{stats(sport_by_year)}}
            <li>{{link(Extreme dates, extreme_dates.tpl)}}</li>
            {{stats(extreme_dates)}}
        </ul>
    </body>
</html>