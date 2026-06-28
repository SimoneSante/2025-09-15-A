from database.DB_connect import DBConnect
from model.piloti import Pilota
from model.arco import Arco
class DAO():

    @staticmethod
    def getAllYears():
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = "SELECT distinct year FROM seasons s  ORDER BY year"

        cursor.execute(query)

        for row in cursor:
            results.append(row["year"])

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_nodi(c,b):
        if c==""or b=="":
            return 0
        conn = DBConnect.get_connection()

        results = []

        cursor = conn.cursor(dictionary=True)
        query = """select d.*
                from drivers d, results r
                where r.raceid in (select raceid 
                                    from races r
                                    where year>=%s and year<=%s) 
                                    and d.driverId =r.driverId 
                                    and r.`position` is not null"""


        cursor.execute(query,(c,b))

        for row in cursor:
            results.append(Pilota(**row))

        cursor.close()
        conn.close()
        return results

    @staticmethod
    def get_archi(lista,mappa,c,b):
        if lista==[]:
            return []

        conn = DBConnect.get_connection()
        placeholders = ",".join(["%s"] * len(lista))
        results = []

        cursor = conn.cursor(dictionary=True)
        query = f"""select least(r1.driverId , r2.driverId ) as id1,
                greatest(r1.driverId , r2.driverId ) as id2,
                count(*) as peso
                from results r1, results r2, races ra
                where r1.driverId in ({placeholders}) and r2.driverId in ({placeholders}) and r1.driverId < r2.driverId  and 
                r1.constructorId=r2.constructorId and r1.raceId =r2.raceId and r1.`position` is not null and r2.`position` is not null and ra.`year` >=%s and ra.`year` <=%s and r1.raceId =ra.raceId and r2.raceId =ra.raceId 
                group by r1.driverId, r2.driverId;"""
        params=lista+lista+[c,b]
        cursor.execute(query, params)

        for row in cursor:
            results.append(Arco(mappa[row["id1"]],mappa[row["id2"]],row["peso"]))

        cursor.close()
        conn.close()
        return results


